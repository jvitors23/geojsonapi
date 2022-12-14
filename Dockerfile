FROM python:3.9.6-alpine
MAINTAINER jvitors23

ENV PYTHONUNBUFFERED 1
ENV POETRY_VERSION=1.2.2
ENV POETRY_VIRTUALENVS_CREATE=false
ENV POETRY_CACHE_DIR='/var/cache/pypoetry'

RUN apk update \
    && apk upgrade \
    && apk add --update --no-cache --virtual \
    build-base \
    gcc \
    libc-dev \
    linux-headers \
    libffi-dev \
    musl-dev \
    zlib \
    zlib-dev \
    bash \
    postgresql-client \
    postgresql-dev \
    curl-dev \
    geos \
    proj \
    gdal

RUN python -m pip install --upgrade pip \
    && pip install "poetry==$POETRY_VERSION" \
    && poetry --version

RUN mkdir /app
WORKDIR /app

COPY . .

RUN poetry install

EXPOSE 8000

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static
# For security (don't run app with root user)
RUN adduser -D user
RUN chown -R user:user /vol/
RUN chmod -R 755 /vol/web
USER user
