from flask import Blueprint
from flask import current_app
from flask import render_template
from flask import Response

from . import db
from . import models

bp = Blueprint("core", __name__)


@bp.route("/robots.txt")
def robots() -> Response:
    return current_app.send_static_file("robots.txt")


@bp.route("/", defaults={"path": ""})
@bp.route("/<path:path>/")
def page(path: str) -> str:
    obj = db.get_or_404(models.Page, path)
    return render_template([f"{path}.html", "page.html"], page=obj)


@bp.route("/people/<path>")
def person(path: str) -> str:
    obj = db.get_or_404(models.Person, path)
    return render_template("person.html", page=obj)


@bp.route("/p/<path>")
def project(path: str) -> str:
    obj = db.get_or_404(models.Project, path)
    return render_template("project.html", page=obj)


@bp.route("/blog/<path:path>")
def blog_post(path: str) -> str:
    obj = db.get_or_404(models.BlogPost, path)
    return render_template("blog.html", page=obj)
