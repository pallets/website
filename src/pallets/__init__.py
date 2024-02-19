from __future__ import annotations


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from werkzeug.middleware.proxy_fix import ProxyFix

db = SQLAlchemy()


def create_app() -> Flask:
    from .load import load_content

    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY="dev",
        SQLALCHEMY_DATABASE_URI="sqlite://",
        FORWARDED=dict(FOR=0, PROTO=0, HOST=0, PORT=0, PREFIX=0),
    )
    app.config.from_prefixed_env()

    db.init_app(app)

    from . import models

    with app.app_context():
        db.create_all()
        load_content(
            app,
            models.Page,
            {
                "blog": models.BlogPost,
                "people": models.Person,
                "projects": models.Project,
            },
        )

    forwarded = app.config["FORWARDED"]

    if forwarded["FOR"] > 0:
        app.wsgi_app = ProxyFix(
            app.wsgi_app,
            x_for=forwarded["FOR"],
            x_proto=forwarded["PROTO"],
            x_host=forwarded["HOST"],
            x_port=forwarded["PORT"],
            x_prefix=forwarded["PREFIX"],
        )

    return app
