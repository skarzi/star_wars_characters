import operator

from django.urls import reverse

import pytest

from rest_framework import status


def _assert_sorted_equal(sequence0, sequence1, **kwargs):
    """Assert if sorted sequences are equal."""
    assert sorted(sequence0, **kwargs) == sorted(sequence1, **kwargs)


@pytest.mark.django_db
class TestPeopleCollectionListCreateAPIView(object):
    view_name = 'collections:people-list'
    url = reverse(view_name)

    def test_create(self, mocker, people_collection, api_client):
        """Ensure create endpoint returns expected data."""
        mocker.patch(
            'apps.collections.services.download_people_collection',
            return_value=people_collection,
        )
        response = api_client.post(self.url)
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['data']['id'] == people_collection.id

    def test_list(self, people_collection_factory, api_client):
        """Ensure list endpoint returns expected data."""
        people_collection_factory.create_batch(11)
        response = api_client.get(self.url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['next']
        assert len(response.data['data'])


@pytest.mark.django_db
class TestPeopleCollectionFieldCountsAPIView(object):
    view_name = 'collections:people_fields_counts-detail'

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
    def test_retrieve_valid_field_names(
        self,
        dummy_people_collection,
        api_client,
        field_names,
        expected_fields_counts,
    ):
        """Ensure retrieve endpoint returns expected data when fields valid."""
        response = api_client.get(
            reverse(
                self.view_name,
                kwargs={
                    'pk': dummy_people_collection.id,
                    'field_names': field_names,
                },
            )
        )
        assert response.status_code == status.HTTP_200_OK
        _assert_sorted_equal(
            response.data['data'],
            expected_fields_counts,
            key=operator.itemgetter('count', *field_names),
        )
