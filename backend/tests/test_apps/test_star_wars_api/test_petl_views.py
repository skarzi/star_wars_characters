import petl
import pytest

from apps.star_wars_api import petl_views


@pytest.fixture(scope='module')
def view_class():
    """``BaseCollectionView`` subclass used in tests."""
    return type(  # noqa: WPS317
        'TestsCollectionView',
        (petl_views.BaseCollectionView,),
        {'collection_name': 'tests', 'field_names': ['id']},
    )


@pytest.fixture
def view(view_class, client):
    """Instance of testing``BaseCollectionView`` subclass."""
    return view_class(client)


def test_url(view, star_wars_api_url):
    """Ensure expected URL is returned."""
    assert view.url.startswith(star_wars_api_url)
    assert view.url.endswith('tests')


def test_iter_empty_response(mocker, client, view):
    """Ensure ``__iter__`` return ``field_names`` when collection empty."""
    response_mock = mocker.Mock()
    response_mock.json.return_value = {'results': []}
    mocker.patch.object(
        client,
        'follow_pagination',
        return_value=[response_mock],
    )
    assert list(view) == [('id',)]


def test_iter_non_empty_response(mocker, client, view):
    """Ensure ``__iter__`` return ``field_names`` and extracted rows."""
    response_mock = mocker.Mock()
    response_mock.json.return_value = {
        'results': [{'id': _id} for _id in range(1, 4)],
    }
    mocker.patch.object(
        client,
        'follow_pagination',
        return_value=[response_mock],
    )
    assert list(view) == [('id',), (1,), (2,), (3,)]


class TestProcessPeopleCollectionView(object):
    @pytest.fixture
    def people_view(self, star_wars_api_url):
        """Object pretending to be ``PeopleCollectionView`` instance."""
        return petl.fromdicts(
            [
                {
                    'name': 'Person 1',
                    'homeworld': 'planets/1',
                    'edited': '2020-08-30T20:58:18.420000Z',
                },
                {
                    'name': 'Person 2',
                    'homeworld': 'planets/4',
                    'edited': '2020-08-31T13:47:18.480000Z',
                },
                {
                    'name': 'Person 3',
                    'homeworld': 'planets/1',
                    'edited': '2020-08-30T20:58:18.420000Z',
                },
                {
                    'name': 'Person 4',
                    'homeworld': 'planets/2',
                    'edited': '2020-08-31T06:31:18.370000Z',
                },
                {
                    'name': 'Person 5',
                    'homeworld': 'planets/1',
                    'edited': '2020-09-01T06:31:18.370000Z',
                },
            ],
            header=('name', 'homeworld', 'edited'),
        )

    @pytest.fixture
    def planets_view(self, star_wars_api_url):
        """Object pretending to be ``PlanetsCollectionView`` instance."""
        return petl.fromdicts(
            [
                {
                    'name': 'Planet {0}'.format(index),
                    'url': 'planets/{0}'.format(index),
                }
                for index in range(1, 5)
            ],
            header=('url', 'name'),
        )

    def test_homeworld(self, people_view, planets_view):
        """Ensure ``homeworld`` field is properly resolved."""
        processed_view = petl_views.process_people_collection_view(
            people_view,
            planets_view,
        ).sort('name')
        expected_homeworlds = [
            'Planet 1',
            'Planet 4',
            'Planet 1',
            'Planet 2',
            'Planet 1',
        ]
        assert list(processed_view['homeworld']) == expected_homeworlds

    def test_edited(self, people_view, planets_view):
        """Ensure ``edited`` field is dropped."""
        processed_view = petl_views.process_people_collection_view(
            people_view,
            planets_view,
        )
        with pytest.raises(petl.FieldSelectionError, match='edited'):
            list(processed_view['edited'])

    def test_date(self, people_view, planets_view):
        """Ensure ``date`` field is properly populated."""
        processed_view = petl_views.process_people_collection_view(
            people_view,
            planets_view,
        ).sort('name')
        expected_dates = [
            '2020-08-30',
            '2020-08-31',
            '2020-08-30',
            '2020-08-31',
            '2020-09-01',
        ]
        assert list(processed_view['date']) == expected_dates
