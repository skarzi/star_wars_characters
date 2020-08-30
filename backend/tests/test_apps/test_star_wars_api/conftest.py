import pytest

from apps.star_wars_api.client import StarWarsAPIClient


@pytest.fixture
def star_wars_api_url(settings):
    """Star Wars API URL used in tests."""
    settings.STAR_WARS_API_URL = 'http://test.star-wars.com/api/people/'
    return settings.STAR_WARS_API_URL


@pytest.fixture
def client():
    """``StarWarsAPIClient`` instance used in tests."""
    return StarWarsAPIClient()
