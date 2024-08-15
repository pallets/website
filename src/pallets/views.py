from __future__ import annotations

import typing as t
from pathlib import Path

import sqlalchemy as sa
from flask import Blueprint
from flask import current_app
from flask import redirect
from flask import render_template
from flask import send_from_directory
from flask import url_for
from werkzeug import Response
from werkzeug.exceptions import NotFound

from . import db
from . import models

bp = Blueprint("core", __name__)


@bp.get("/robots.txt")
def robots() -> Response:
    return current_app.send_static_file("robots.txt")


@bp.get("/static/content/<path:path>")
def static_content(path: str) -> Response:
    return send_from_directory(
        Path(current_app.root_path).parent.parent / "content", path
    )


@bp.get("/", defaults={"path": ""})
@bp.get("/<path:path>")
def page(path: str) -> str | Response:
    page_path = path.removesuffix("/")
    obj = db.session.get(models.Page, page_path)

    if obj is None:
        raise NotFound()

    if path.endswith("/"):
        if not obj.is_dir:
            return current_app.redirect(current_app.url_for(".page", path=path[:-1]))
    elif path:
        if obj.is_dir:
            return current_app.redirect(current_app.url_for(".page", path=f"{path}/"))

    template_path = f"{page_path}/index.html" if obj.is_dir else f"{page_path}.html"
    t = render_template([template_path, "page.html"], page=obj)
    return t


@bp.route("/people/<path:path>")
def person(path: str) -> str:
    path = path.removesuffix("/")
    obj = db.session.get(models.Person, path)

    if obj is None:
        raise NotFound()

    return render_template("person.html", page=obj)


@bp.route("/projects/<path:path>")
def project(path: str) -> str:
    path = path.removesuffix("/")
    obj = db.session.get(models.Project, path)

    if obj is None:
        raise NotFound()

    return render_template("project.html", page=obj)


@bp.route("/p/<path:path>")
def project_redirect(path: str) -> Response:
    return redirect(url_for(".project", path=path))


@bp.route("/blog/")
def blog_index() -> str:
    posts = db.session.scalars(
        sa.select(models.BlogPost).order_by(models.BlogPost.published.desc())
    )
    return render_template("blog/index.html", posts=posts)


@bp.route("/blog/<path:path>")
def blog_post(path: str) -> str:
    path = path.removesuffix("/")
    obj = db.session.get(models.BlogPost, path)

    if obj is None:
        raise NotFound()

    return render_template("blog/post.html", page=obj)


@bp.route("/blog/feed.xml")
def blog_feed() -> tuple[str, dict[str, t.Any]]:
    return models.BlogPost.make_feed(), {"content-type": "application/atom+xml"}
