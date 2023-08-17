FROM python:alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV POETRY_VERSION=1.4.0
ENV POETRY_HOME=/opt/poetry
ENV POETRY_VENV=/opt/poetry-venv
ENV POETRY_CACHE_DIR=/opt/.cache

# Add Poetry to PATH
ENV PATH="${PATH}:${POETRY_VENV}/bin"

RUN apk update && \
    apk upgrade && \
    apk --no-cache add curl

COPY ./ ./

RUN curl -sSL https://install.python-poetry.org/ | python3 - && \
    poetry install --no-interaction --no-cache

WORKDIR /app

EXPOSE 80

ENTRYPOINT [ "poetry", "run", "python3  ", "manage.py", "runserver", "0.0.0.0:80" ]
