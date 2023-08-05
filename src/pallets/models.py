from __future__ import annotations

import typing as t

import sqlalchemy as sa
import sqlalchemy.orm as sa_orm

from . import db


class Page(db.Model):
    path = sa.Column(sa.String, primary_key=True)
    content = sa.Column(sa.String, nullable=False)


class Person(db.Model):
    path = sa.Column(sa.String, primary_key=True)
    content = sa.Column(sa.String)
    name = sa.Column(sa.String, nullable=False)
    nickname = sa.Column(sa.String)
    pronouns = sa.Column(sa.String)
    picture = sa.Column(sa.String)
    location = sa.Column(sa.String)
    links = sa.Column(sa.JSON, nullable=False, default=lambda: {})
    tags = sa.Column(sa.JSON, nullable=False, default=lambda: [])
    lead = sa.Column(sa.Boolean, nullable=False, default=False)
    alumni = sa.Column(sa.Boolean, nullable=False, default=False)


class BlogPost(db.Model):
    path = sa.Column(sa.String, primary_key=True)
    content = sa.Column(sa.String, nullable=False)
    author_path = sa.Column(sa.ForeignKey(Person.path))
    author = sa_orm.relationship(Person)
    published = sa.Column(sa.DateTime, nullable=False)
    updated = sa.Column(sa.DateTime)
    tags = sa.Column(sa.JSON, nullable=False, default=lambda: [])

    def __init__(self, **kwargs: t.Any) -> None:
        kwargs["author_path"] = f"people/{kwargs.pop('author')}"
        super().__init__(**kwargs)
