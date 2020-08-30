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

.PHONY: test
test: lint_python lint_django
