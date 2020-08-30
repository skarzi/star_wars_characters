FROM python:3.8.5-slim as development_build

ARG DJANGO_ENV
ARG USER_ID=1000

ENV DJANGO_ENV=${DJANGO_ENV} \
  # user
  USER_ID=${USER_ID} \
  HOME=/home/django \
  # dockerize
  DOCKERIZE_VERSION=v0.6.1 \
  # python
  PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  # pip
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  # poetry
  POETRY_VERSION=1.0.10 \
  POETRY_CACHE_DIR=/var/cache/pypoetry

RUN apt-get -qq update \
  && apt-get -qq -y --fix-missing install \
     bash \
     curl \
     gcc \
     gettext \
     git \
     libcairo2-dev \
     libpq-dev \
     make \
     musl-dev \
     openssl \
     tini \
  && apt-get -qq -y autoremove \
  && apt-get -qq -y clean \
  && rm -rf /var/lib/apt/lists/* \
  # install dockerize
  && curl \
      --location \
      --silent \
      --output "./dockerize-linux-amd64-${DOCKERIZE_VERSION}.tar.gz" \
      "https://github.com/jwilder/dockerize/releases/download/${DOCKERIZE_VERSION}/dockerize-linux-amd64-${DOCKERIZE_VERSION}.tar.gz" \
  && tar \
      -C /usr/local/bin \
      -xzvf "./dockerize-linux-amd64-${DOCKERIZE_VERSION}.tar.gz" \
  && rm "./dockerize-linux-amd64-${DOCKERIZE_VERSION}.tar.gz" \
  # install poetry
  && pip install --upgrade pip setuptools wheel \
  && pip install "poetry==${POETRY_VERSION}"

# create the user and group to run the Django application as
RUN addgroup --system --gid ${USER_ID} django \
    && adduser --system --home ${HOME} --uid ${USER_ID} --ingroup django django

COPY ./.devops/docker/backend/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

COPY ./.devops/docker/backend/start.sh /start.sh
RUN chmod +x /start.sh

ENTRYPOINT ["/usr/bin/tini", "--", "/entrypoint.sh"]
CMD ["/start.sh"]

WORKDIR /app

# install python dependencies
COPY ./backend/poetry.lock ./backend/pyproject.toml /app/
RUN poetry config virtualenvs.create false \
  && poetry install \
    $(if [ "${DJANGO_ENV}" = 'production' ]; then echo '--no-dev'; fi) \
    --no-interaction \
    --no-ansi \
  # cleaning poetry installation's cache for production
  && if [ "${DJANGO_ENV}" = 'production' ]; then rm -rf "${POETRY_CACHE_DIR}"; fi


RUN chown -R django /app /home/django
USER django


# PRODUCTION ONLY STAGE
FROM development_build as production_build

USER root

# override `/start.sh` to serve app with `gunicorn`
COPY ./.devops/docker/backend/gunicorn.sh /start.sh
RUN chmod +x /start.sh

COPY --chown=django:django . /app
USER django
