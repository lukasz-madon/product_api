FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN pip install poetry

COPY poetry.lock pyproject.toml /app/

RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

COPY . /app
