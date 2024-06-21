from __future__ import annotations

import posixpath
import typing as t
from datetime import datetime

import sqlalchemy as sa
import sqlalchemy.orm as orm
from markupsafe import Markup

from . import Model
from .markdown import render_content


class BasePage(Model):
    __abstract__ = True

    path: orm.Mapped[str] = orm.mapped_column(primary_key=True)
    is_dir: orm.Mapped[bool] = orm.mapped_column(default=False)
    content: orm.Mapped[str | None]

    @property
    def content_html(self) -> str:
        if self.content is None:
            return Markup()

        return Markup(render_content(self.content, posixpath.dirname(self.path)))


class PrefixPage(BasePage):
    __abstract__ = True

    def __init__(self, **kwargs: t.Any) -> None:
        kwargs["path"] = kwargs["path"].partition("/")[2]
        super().__init__(**kwargs)


class Page(BasePage):
    __tablename__ = "page"


class Person(PrefixPage):
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


class Project(PrefixPage):
    __tablename__ = "project"
    name: orm.Mapped[str]
    logo: orm.Mapped[str | None]
    pypi: orm.Mapped[str]
    github: orm.Mapped[str]
    docs: orm.Mapped[str]

    def __init__(self, **kwargs: t.Any) -> None:
        name = kwargs["path"].partition("/")[2]
        kwargs.setdefault("pypi", name)
        kwargs.setdefault("github", name)
        kwargs.setdefault("docs", name)
        super().__init__(**kwargs)


class BlogPost(BasePage):
    __tablename__ = "blog_post"
    content: orm.Mapped[str]
    author_path: orm.Mapped[str | None] = orm.mapped_column(sa.ForeignKey(Person.path))
    author: orm.Mapped[Person | None] = orm.relationship()
    published: orm.Mapped[datetime]
    updated: orm.Mapped[datetime]
    tags: orm.Mapped[list[str]] = orm.mapped_column(sa.JSON, default=list)

    def __init__(self, **kwargs: t.Any) -> None:
        kwargs["author_path"] = kwargs.pop("author")
        path = kwargs["path"].partition("/")[2]
        published = kwargs["published"]
        kwargs["path"] = f"{published:%Y/%m}/{path}"
        super().__init__(**kwargs)
