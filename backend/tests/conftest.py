import pytest

from pytest_django.lazy_django import skip_if_no_django
from pytest_factoryboy import register
from rest_framework.test import (
    APIClient,
    APIRequestFactory,
)

from tests import factories


def pytest_sessionstart(session):
    """Pytest hook called on session start."""
    register_factories()


def register_factories() -> None:
    """Register ``factory_boy`` factories."""
    register(factories.PeopleCollectionFactory)


@pytest.fixture
def api_client() -> APIClient:
    """REST framework test ``APIClient`` instance."""
    skip_if_no_django()
    return APIClient()


@pytest.fixture
def api_rf() -> APIClient:
    """REST framework test ``APIRequestFactory`` instance."""
    skip_if_no_django()
    return APIRequestFactory()
