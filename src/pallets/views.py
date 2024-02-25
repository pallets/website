from pathlib import Path

from flask import Blueprint
from flask import current_app
from flask import render_template
from flask import Response
from flask import send_from_directory

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
    obj = db.get_or_404(models.Page, page_path)

    if path.endswith("/"):
        if not obj.is_dir:
            return current_app.redirect(current_app.url_for(".page", path=path[:-1]))
    elif path:
        if obj.is_dir:
            return current_app.redirect(current_app.url_for(".page", path=f"{path}/"))

    template_path = f"{page_path}/index.html" if obj.is_dir else f"{page_path}.html"
    print(template_path)
    t = render_template([template_path, "page.html"], page=obj)
    return t


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
