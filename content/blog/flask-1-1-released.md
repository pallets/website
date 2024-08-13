~~~~toml
title = "Flask 1.1 Released"
author_name = "David Lord"
published = 2019-07-04
tags = ["releases"]
~~~~

The Pallets team is pleased to release [Flask](/p/flask/) 1.1. The
latest version is 1.1.1. Version 1.0.4 was also released.

-   Drop support for Python 3.4.
-   Bump minimum Werkzeug version to 0.15.
-   The way error handlers for `InternalServerError` and `500` work has
    been made more consistent. See below for more information.
-   `app.logger` once again takes the same name as `app.name`, reverting
    1.0.x's behavior of hard-coding `"flask.app"`. See below for more
    information.
-   `jsonify` supports Python's [`dataclasses`](https://docs.python.org/3/library/dataclasses.html).
-   Returning a `dict` from a view function will produce a JSON
    response. This makes it even easier to get started building an API.
-   A clearer error message is shown when a view returns an unsupported
    type.
-   URL routing is performed after the request context is pushed. This
    allows custom URL converters to access `current_app` and `request`.
    This makes it possible to implement converters such as one that
    queries the database for a model based on the ID in the URL.
-   CLI commands can be registered with blueprints using the new
    `bp.cli` attribute. These will be available as nested commands, for
    example `flask user create`.

[**Read the changelog**](https://flask.palletsprojects.com/en/1.1.x/changelog/)
for the full list of changes. Be sure to check the notes for the 1.0.x
versions as well.


Change to Error Handling
