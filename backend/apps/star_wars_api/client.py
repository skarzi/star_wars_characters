import typing

import requests

from requests.structures import CaseInsensitiveDict


def url_join(base_url: str, *args: str, append_slash: bool = False) -> str:
    """Join base_url and args items into one URL.

    Append slash at the end of url if `append_slash` is truthy.
    """
    url = '/'.join(
        str(path).strip('/')
        for path in (base_url, *args)
    )
    return '{0}/'.format(url) if append_slash else url


class StarWarsAPIClient(object):  # noqa: WPS214
    """Star Wars API client using ``requests.Session``."""

    default_headers: typing.ClassVar[CaseInsensitiveDict] = CaseInsensitiveDict(
        {'Content-Type': 'application/json', 'Accept': 'application/json'},
    )

    def __init__(
        self,
        url: str,
        *,
        timeout: int = 60,
        verify_ssl: bool = True,
    ) -> None:
        """Initialize ``request.Session`` and set API URL."""
        self.url = url
        self.timeout = int(timeout)
        self.verify_ssl = verify_ssl
        self._session = requests.Session()
        self._session.headers = self.default_headers

    def request(self, method: str, path: str, **kwargs) -> requests.Response:
        """Perform an HTTP request to Star Wars API."""
        url = url_join(self.url, path)
        kwargs.setdefault('timeout', self.timeout)
        kwargs.setdefault('verify', self.verify_ssl)
        return self._session.request(method=method, url=url, **kwargs)

    def get(self, path: str, **kwargs) -> requests.Response:
        """Perform HTTP GET request to Star Wars API."""
        return self.request('GET', path=path, **kwargs)

    def options(self, path: str, **kwargs) -> requests.Response:
        """Perform HTTP OPTIONS request to Star Wars API."""
        return self.request('OPTIONS', path=path, **kwargs)

    def head(self, path: str, **kwargs) -> requests.Response:
        """Perform HTTP HEAD request to Star Wars API."""
        return self.request('HEAD', path=path, **kwargs)

    def post(self, path: str, **kwargs) -> requests.Response:
        """Perform HTTP POST request to Star Wars API."""
        return self.request('POST', path=path, **kwargs)

    def put(self, path: str, **kwargs) -> requests.Response:
        """Perform HTTP PUT request to Star Wars API."""
        return self.request('PUT', path=path, **kwargs)

    def patch(self, path: str, **kwargs) -> requests.Response:
        """Perform HTTP PATCH request to Star Wars API."""
        return self.request('PATCH', path=path, **kwargs)

    def delete(self, path: str, **kwargs) -> requests.Response:
        """Perform HTTP DELETE request to Star Wars API."""
        return self.request('DELETE', path=path, **kwargs)
