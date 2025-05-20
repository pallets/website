FROM python:3.13-slim AS builder
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
WORKDIR /app
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-install-project --no-editable --compile-bytecode

FROM python:3.13-slim
EXPOSE 8000
WORKDIR /app
COPY --from=builder /app/.venv /app/.venv
ADD . /app
ENV PATH=/app/.venv/bin:$PATH
ENV FLASK_APP=pallets
RUN --mount=type=cache,target=/root/.cache/uv \
    uv pip install -e .
CMD ["gunicorn", "-c", "gunicorn_conf.py", "pallets:create_app()"]
