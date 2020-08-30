SHELL:=/usr/bin/env bash


.PHONY: lint_python
lint_python:
	flake8 .
	mypy .

.PHONY: lint_django
lint_django:
	# check migrations graph
	python manage.py makemigrations --dry-run --check
	# run django check
	python manage.py check --fail-level=WARNING

.PHONY: unit
unit:
	pytest --dead-fixtures --dup-fixtures
	pytest

.PHONY: test
test: lint_python lint_django unit
