from __future__ import annotations

from flask import Flask
from flask_sqlalchemy_lite import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from werkzeug.middleware.proxy_fix import ProxyFix


class Model(DeclarativeBase):
    pass


db = SQLAlchemy()


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY="dev",
        SERVER_NAME="127.0.0.1:5000",
        SQLALCHEMY_ENGINES={"default": "sqlite://"},
        FORWARDED=dict(FOR=0, PROTO=0, HOST=0, PORT=0, PREFIX=0),
    )
    app.config.from_prefixed_env()

    db.init_app(app)

    from . import models
    from . import views
    from .load import load_content

    app.register_blueprint(views.bp)

    with app.app_context():
        Model.metadata.create_all(db.engine)
        load_content(
            app,
            models.Page,
            {
                "blog": models.BlogPost,
                "people": models.Person,
                "projects": models.Project,
            },
        )
        # cache the feed
        models.BlogPost.make_feed()

    forwarded = app.config["FORWARDED"]

    if forwarded["FOR"] > 0:
        app.wsgi_app = ProxyFix(  # type: ignore[method-assign]
            app.wsgi_app,
            x_for=forwarded["FOR"],
            x_proto=forwarded["PROTO"],
            x_host=forwarded["HOST"],
            x_port=forwarded["PORT"],
            x_prefix=forwarded["PREFIX"],
        )

    return app
