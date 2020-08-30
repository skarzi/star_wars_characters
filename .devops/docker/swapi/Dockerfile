FROM python:2.7.8-slim

RUN apt-get -qq update \
    && apt-get -qq --force-yes install \
        bash \
        curl \
        gcc \
        gettext \
        # pylibmc
        libmemcached-dev \
        # psycopg
        libpq-dev \
        make \
        vim \
    && apt-get -qq --force-yes autoremove \
    && apt-get -qq --force-yes clean \
    && rm -rf /var/lib/apt/lists/* \
    && pip install -U pip

WORKDIR /app

COPY ./swapi/requirements.txt /app/requirements.txt
COPY ./swapi/Makefile /app/Makefile
RUN pip install wheel && make install
