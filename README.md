# Star Wars API people resource explorer

API and web app that allow to explore Star Wars API people resource.

## Developing locally

> `docker` and `docker-compose` is necessary to work on this project.

Every command listed below should be run from repository root.
Firstly setup `docker-compose.override.yml` properly to your OS:

```bash
cp \
    .devops/docker/docker-compose.override.yml.example \
    docker-compose.override.yml
```

To build `docker` images that won't mess up with your local file permissions
you need to find your current user id - `UID`, by running following command:

```bash
echo "${UID}"
```

Replace all repetitions of `!!UID!!` value in `docker-compose.override.yml`.

Finally let's ensure that all host ports listed in `ports` services of sections
are available.

To build all services images simply run:

```bash
docker-compose build
```

To setup `swapi` service use following commands:

NOTE: You will be prompted for superuser `username` and `password`,
please provide it!

```bash
docker-compose run --rm swapi make build load_data
```

To setup backend `app` service run following commands:

```bash
docker-compose run --rm app python manage.py migrate --no-input
docker-compose run --rm app python manage.py collectstatic --no-input
```

Then, you can run all services:

```bash
docker-compose up --detach
```

WEB UI and REST API services ports are forwarded from container to localhost:

+ [localhost:8080](http://localhost:8080) - WEB UI
+ [localhost:8000](http://localhost:8000) - REST API, you can verify it's
  health on [localhost:8000/healthz](http://localhost:8000/healthz)
+ [localhost:8001](http://localhost:8001) - Star Wars API

Linters and unit tests of backend service can be run with executing:

```bash
docker-compose run --rm app make test
```
