import operator

import petl
import pytest

from apps.collections import services


@pytest.mark.django_db
def test_download_people_collection(mocker, client):
    """Ensure proper ``PeopleCollection`` instance is created."""
    mocker.patch(
        'apps.star_wars_api.petl_views.process_people_collection_view',
        return_value=petl.fromdicts(
            dicts=[{'id': 1, 'name': 'Name 1'}, {'id': 2, 'name': 'Name 2'}],
            header=('id', 'name'),
        ),
    )
    instance = services.download_people_collection(client)
    with instance.file.open(mode='r') as csv_file:
        assert csv_file.read() == 'id,name\n1,Name 1\n2,Name 2\n'


@pytest.mark.parametrize(('field_names', 'expected_fields_counts'), [
    (
        ('field0',),
        [{'field0': '0', 'count': 3}, {'field0': '1', 'count': 2}],
    ),
    (
        ('field1',),
        [
            {'field1': '11', 'count': 2},
            {'field1': '10', 'count': 2},
            {'field1': '12', 'count': 1},
        ],
    ),
    (
        ('field0', 'field1'),
        [
            {'field0': '1', 'field1': '11', 'count': 1},
            {'field0': '1', 'field1': '10', 'count': 1},
            {'field0': '0', 'field1': '12', 'count': 1},
            {'field0': '0', 'field1': '10', 'count': 1},
            {'field0': '0', 'field1': '11', 'count': 1},
        ],
    ),
])
def test_count_fields(
    assert_sorted_equal,
    dummy_petl_view,
    field_names,
    expected_fields_counts,
):
    """Ensure fields values are properly counted."""
    assert_sorted_equal(
        services.count_fields(dummy_petl_view, field_names),
        expected_fields_counts,
        key=operator.itemgetter('count', *field_names),
    )
