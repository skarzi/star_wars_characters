import pytest


def test_request(mocker, client, star_wars_api_url):
    """Ensure proper HTTP requests is trigerred."""
    method = 'OPTIONS'
    allow_redirects = False
    mocker.patch.object(client, '_session')
    client.request(method, star_wars_api_url, allow_redirects=allow_redirects)
    request_kwargs = {
        'method': method,
        'url': star_wars_api_url,
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
def test_http_method(mocker, client, star_wars_api_url, http_method):
    """Ensure proper HTTP requests is trigerred for each HTTP method."""
    request_mock = mocker.patch.object(client, 'request')
    getattr(client, http_method.lower())(star_wars_api_url)
    request_mock.assert_called_once_with(http_method, url=star_wars_api_url)


def test_follow_pagination(mocker, client, star_wars_api_url):
    """Ensure ``follow_pagination`` returns proper responses."""
    responses_number = 5
    fake_responses = [
        mocker.Mock(**{  # noqa: WPS445, WPS517
            'json.return_value': {
                'next': '{0}?page={1}'.format(star_wars_api_url, page_number),
            },
        })
        for page_number in range(1, responses_number + 1)
    ]
    fake_responses[-1].json.return_value['next'] = None
    mocker.patch.object(client, 'request', side_effect=fake_responses)
    responses = list(client.follow_pagination(client.get(star_wars_api_url)))
    assert len(responses) == responses_number
