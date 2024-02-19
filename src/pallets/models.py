from __future__ import annotations

import typing as t

import sqlalchemy as sa
import sqlalchemy.orm as sa_orm
from markupsafe import Markup

from . import db
from .markdown import markdown


class BasePage(db.Model):
    __abstract__ = True

    path = sa.Column(sa.String, primary_key=True)
    content = sa.Column(sa.String)

    @property
    def content_html(self) -> str:
        return Markup(markdown.convert(self.content))


class PrefixPage(BasePage):
    __abstract__ = True

    def __init__(self, **kwargs: t.Any) -> None:
        kwargs["path"] = kwargs["path"].partition("/")[2]
        super().__init__(**kwargs)


class Page(BasePage):
    pass


class Person(PrefixPage):
    name = sa.Column(sa.String, nullable=False)
    nickname = sa.Column(sa.String)
    pronouns = sa.Column(sa.String)
    picture = sa.Column(sa.String)
    location = sa.Column(sa.String)
    links = sa.Column(sa.JSON, nullable=False, default=lambda: {})
    tags = sa.Column(sa.JSON, nullable=False, default=lambda: [])
    lead = sa.Column(sa.Boolean, nullable=False, default=False)
    alumni = sa.Column(sa.Boolean, nullable=False, default=False)


class Project(PrefixPage):
    name = sa.Column(sa.String, nullable=False)
    logo = sa.Column(sa.String)
    pypi = sa.Column(sa.String, nullable=False)
    github = sa.Column(sa.String, nullable=False)
    docs = sa.Column(sa.String, nullable=False)

    def __init__(self, **kwargs: t.Any) -> None:
        name = kwargs["path"].partition("/")[2]
        kwargs.setdefault("pypi", name)
        kwargs.setdefault("github", name)
        kwargs.setdefault("docs", name)
        super().__init__(**kwargs)


class BlogPost(BasePage):
    path = sa.Column(sa.String, primary_key=True)
    content = sa.Column(sa.String, nullable=False)
    author_path = sa.Column(sa.ForeignKey(Person.path))
    author = sa_orm.relationship(Person)
    published = sa.Column(sa.DateTime, nullable=False)
    updated = sa.Column(sa.DateTime)
    tags = sa.Column(sa.JSON, nullable=False, default=lambda: [])

    def __init__(self, **kwargs: t.Any) -> None:
        kwargs["author_path"] = kwargs.pop("author")
        path = kwargs["path"].partition("/")[2]
        published = kwargs["published"]
        kwargs["path"] = f"{published:%Y/%m}/{path}"
        super().__init__(**kwargs)
