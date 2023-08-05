from __future__ import annotations

import os
import tomllib
import typing as t
from pathlib import Path

from flask import Flask

from . import db


def load_content(
    app: Flask, base_model: type[t.Any], path_models: dict[str, type[t.Any]]
) -> None:
    base = os.fspath(Path(app.root_path).parent.parent / "content")

    for parent, _, files in os.walk(base):
        relative = os.path.relpath(parent, base).lstrip(".").replace("\\", "/")
        rel_current = relative

        while rel_current:
            if rel_current in path_models:
                path_models[relative] = path_model = path_models[rel_current]
                break

            rel_current = os.path.dirname(rel_current)
        else:
            path_models[relative] = path_model = base_model

        for file in files:
            name, ext = os.path.splitext(file)

            if file[0] == "_":
                continue

            if ext == ".md":
                data = parse_md(os.path.join(parent, file))
            elif ext == ".toml":
                with open(os.path.join(parent, file), "rb") as f:
                    data = tomllib.load(f)
            else:
                continue

            if name == "index":
                model = path_models[os.path.dirname(relative)]
                data["path"] = relative
            else:
                model = path_model
                data["path"] = f"{relative}/{name}".removeprefix("/")

            db.session.add(model(**data))

        db.session.commit()


def parse_md(file: str | os.PathLike) -> dict[str, t.Any]:
    data = Path(file).read_text()

    if data.startswith("~~~~toml"):
        reading_toml = True
        toml_lines = []
        content_lines = []

        for line in data.splitlines():
            if reading_toml:
                toml_lines.append(line)

                if line == "~~~~":
                    reading_toml = False
            else:
                content_lines.append(line)

        out = tomllib.loads("\n".join(toml_lines))
        out["content"] = "\n".join(content_lines)
        return out

    return {"content": data}
