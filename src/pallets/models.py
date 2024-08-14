from __future__ import annotations

import posixpath
import typing as t
from datetime import datetime
from datetime import UTC

import sqlalchemy as sa
import sqlalchemy.orm as orm
from feedgen.feed import FeedGenerator
from flask import url_for

from . import db
from . import Model
from .markdown import render_content


class BasePage(Model):
    content_prefix: str = ""
    __abstract__ = True
    path: orm.Mapped[str] = orm.mapped_column(primary_key=True)
    is_dir: orm.Mapped[bool] = orm.mapped_column(default=False)
    content: orm.Mapped[str | None]
    content_html: orm.Mapped[str] = orm.mapped_column(default="")

    def __init__(self, **kwargs: t.Any) -> None:
        kwargs["path"] = kwargs["path"].removeprefix(f"{self.content_prefix}/")
        super().__init__(**kwargs)

        if self.content:
            path = posixpath.join(self.content_prefix, posixpath.dirname(self.path))
            self.content_html = render_content(self.content, path)


class Page(BasePage):
    __tablename__ = "page"


class Person(BasePage):
    content_prefix = "people"
    __tablename__ = "person"
    name: orm.Mapped[str]
    nickname: orm.Mapped[str | None]
    pronouns: orm.Mapped[str | None]
    picture: orm.Mapped[str | None]
    location: orm.Mapped[str | None]
    links: orm.Mapped[dict[str, str]] = orm.mapped_column(sa.JSON, default=dict)
    tags: orm.Mapped[list[str]] = orm.mapped_column(sa.JSON, default=list)
    lead: orm.Mapped[bool] = orm.mapped_column(default=False)
    alumni: orm.Mapped[bool] = orm.mapped_column(default=False)


class Project(BasePage):
    content_prefix = "projects"
    __tablename__ = "project"
    name: orm.Mapped[str]
    logo: orm.Mapped[str | None]
    pypi: orm.Mapped[str]
    github: orm.Mapped[str]
    docs: orm.Mapped[str]

    def __init__(self, **kwargs: t.Any) -> None:
        name = kwargs["path"].partition("/")[2]
        kwargs.setdefault("pypi", f"https://pypi.org/project/{name}/")
        kwargs.setdefault("github", f"https://github.com/pallets/{name}")
        kwargs.setdefault("docs", f"https://{name}.palletsprojects.com")
        super().__init__(**kwargs)


class BlogPost(BasePage):
    content_prefix = "blog"
    __tablename__ = "blog_post"
    title: orm.Mapped[str]
    content: orm.Mapped[str]  # pyright: ignore
    author_name: orm.Mapped[str]
    published: orm.Mapped[datetime]
    updated: orm.Mapped[datetime]
    tags: orm.Mapped[list[str]] = orm.mapped_column(sa.JSON, default=list)

    def __init__(self, **kwargs: t.Any) -> None:
        kwargs.setdefault("updated", kwargs["published"])
        super().__init__(**kwargs)

    @classmethod
    def make_feed(cls) -> str:
        global _cached_feed

        if _cached_feed is not None:
            return _cached_feed

        posts = db.session.scalars(
            sa.select(cls).order_by(cls.published.desc()).limit(10)
        ).all()
        fg = FeedGenerator()
        fg.id(url_for("core.blog_index", _external=True))
        fg.title("Pallets Blog")
        fg.icon(url_for("static", filename="pallets.png", _external=True))
        fg.updated(max(p.updated for p in posts).replace(tzinfo=UTC))
        fg.author(name="Pallets Team")
        fg.link(href=url_for("core.blog_index", _external=True))
        fg.link(href=url_for("core.blog_feed", _external=True), rel="self")

        for post in posts:
            fe = fg.add_entry(order="append")
            fe.id(url_for("core.blog_post", path=post.path, _external=True))
            fe.title(post.title)
            fe.published(post.published.replace(tzinfo=UTC))
            fe.updated(post.updated.replace(tzinfo=UTC))
            fe.author(name=post.author_name)
            # This should be escaped according to the Atom spec, but my feed
            # reader doesn't display that correctly.
            fe.content(post.content_html, type="html")
            fe.link(
                href=url_for("core.blog_post", path=post.path, _external=True),
                rel="alternate",
            )

        _cached_feed = t.cast(str, fg.atom_str(pretty=True).decode())
        return _cached_feed


_cached_feed: str | None = None
