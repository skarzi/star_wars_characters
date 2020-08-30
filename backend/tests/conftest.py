from pytest_factoryboy import register

from tests import factories


def pytest_sessionstart(session):
    """Pytest hook called on session start."""
    register_factories()


def register_factories() -> None:
    """Register ``factory_boy`` factories."""
    register(factories.CollectionDownloadFactory)
