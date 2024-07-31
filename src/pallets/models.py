from __future__ import annotations

import posixpath
import typing as t
from datetime import datetime

import sqlalchemy as sa
import sqlalchemy.orm as orm

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
