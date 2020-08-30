import pytest

from apps.star_wars_api.urls import url_join


class TestURLJoin(object):
    host = 'https://foo-bar.ni'
    expected_url = '{0}/monty/python'.format(host)

    @pytest.mark.parametrize(('host', 'path'), [
        (host, 'monty/python'),
        (host, '/monty/python'),
        ('{0}/'.format(host), 'monty/python'),
        ('{0}/'.format(host), '/monty/python'),
    ])
    def test_single_argument(self, host, path):
        """Ensure ``base_url`` is properly joined with single argument."""
        assert url_join(host, path) == self.expected_url

    def test_append_slash(self):
        """Ensure trailing slash is added when ``append_slash`` truthy."""
        url = url_join(self.host, 'monty/python', append_slash=True)
        assert url == '{0}/'.format(self.expected_url)

    def test_multiple_args(self):
        """Ensure ``base_url`` is properly joined with multiple ``args``."""
        url = url_join(self.host, 'monty/python', 'and-holy/', 'grail')
        assert url == '{0}/and-holy/grail'.format(self.expected_url)
