import pytest

from apps.star_wars_api.client import StarWarsAPIClient


@pytest.fixture
def star_wars_api_url():
    """Star Wars API URL used in tests."""
    return 'http://test.star-wars.com/api/'


@pytest.fixture
def client(star_wars_api_url):
    """``StarWarsAPIClient`` instance used in tests."""
    return StarWarsAPIClient(star_wars_api_url)


def test_request(mocker, client, star_wars_api_url):
    """Ensure proper HTTP requests is trigerred."""
    method = 'OPTIONS'
    path = 'search'
    allow_redirects = False
    mocker.patch.object(client, '_session')
    client.request(method, path, allow_redirects=allow_redirects)
    request_kwargs = {
        'method': method,
        'url': '{0}{1}'.format(star_wars_api_url, path),
        'timeout': client.timeout,
        'verify': client.verify_ssl,
        'allow_redirects': allow_redirects,
    }
    client._session.request.assert_called_once_with(  # noqa: WPS437
        **request_kwargs,
    )


@pytest.mark.parametrize('http_method', [
    'GET',
    'OPTIONS',
    'HEAD',
    'POST',
    'PUT',
    'PATCH',
    'DELETE',
])
def test_http_method(mocker, client, http_method):
    """Ensure proper HTTP requests is trigerred for each HTTP method."""
    path = 'test'
    request_mock = mocker.patch.object(client, 'request')
    getattr(client, http_method.lower())(path)
    request_mock.assert_called_once_with(http_method, path=path)
