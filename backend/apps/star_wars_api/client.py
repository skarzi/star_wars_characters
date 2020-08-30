from typing import (
    ClassVar,
    Iterator,
)

import requests

from requests.structures import CaseInsensitiveDict


class StarWarsAPIClient(object):  # noqa: WPS214
    """Star Wars API client using ``requests.Session``."""

    default_headers: ClassVar[CaseInsensitiveDict] = CaseInsensitiveDict(
        {'Content-Type': 'application/json', 'Accept': 'application/json'},
    )

    def __init__(
        self,
        *,
        timeout: int = 60,
        verify_ssl: bool = True,
    ) -> None:
        """Initialize ``request.Session``."""
        self.timeout = int(timeout)
        self.verify_ssl = verify_ssl
        self._session = requests.Session()
        self._session.headers = self.default_headers

    def follow_pagination(
        self,
        response: requests.Response,
    ) -> Iterator[requests.Response]:
        """Follow pagination of Star Wars API ``request``."""
        yield response

        while response.json().get('next', None):
            response = self.get(response.json()['next'])
            yield response

    def request(self, method: str, url: str, **kwargs) -> requests.Response:
        """Perform an HTTP request to Star Wars API."""
        kwargs.setdefault('timeout', self.timeout)
        kwargs.setdefault('verify', self.verify_ssl)
        return self._session.request(method=method, url=url, **kwargs)

    def get(self, url: str, **kwargs) -> requests.Response:
        """Perform HTTP GET request to Star Wars API."""
        return self.request('GET', url=url, **kwargs)

    def options(self, url: str, **kwargs) -> requests.Response:
        """Perform HTTP OPTIONS request to Star Wars API."""
        return self.request('OPTIONS', url=url, **kwargs)

    def head(self, url: str, **kwargs) -> requests.Response:
        """Perform HTTP HEAD request to Star Wars API."""
        return self.request('HEAD', url=url, **kwargs)

    def post(self, url: str, **kwargs) -> requests.Response:
        """Perform HTTP POST request to Star Wars API."""
        return self.request('POST', url=url, **kwargs)

    def put(self, url: str, **kwargs) -> requests.Response:
        """Perform HTTP PUT request to Star Wars API."""
        return self.request('PUT', url=url, **kwargs)

    def patch(self, url: str, **kwargs) -> requests.Response:
        """Perform HTTP PATCH request to Star Wars API."""
        return self.request('PATCH', url=url, **kwargs)

    def delete(self, url: str, **kwargs) -> requests.Response:
        """Perform HTTP DELETE request to Star Wars API."""
        return self.request('DELETE', url=url, **kwargs)
