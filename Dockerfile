FROM python:3.12 as build
WORKDIR /opt
RUN python -m venv --upgrade-deps venv
COPY requirements requirements
RUN venv/bin/pip install -r requirements/base.txt

FROM python:3.12-slim as deploy
RUN useradd project
USER project
EXPOSE 8000
ENV PATH=/opt/venv/bin:$PATH \
    FLASK_APP=pallets
USER root
COPY --from=build /opt/venv /opt/venv
WORKDIR /opt
COPY --chown=1000:1000 . project
RUN venv/bin/pip install -e project
COPY gunicorn_conf.py .
USER project
CMD ["gunicorn", "-c", "gunicorn_conf.py", "pallets:create_app()"]
