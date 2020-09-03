import operator

from django.urls import reverse

import pytest

from rest_framework import status


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

    def test_retrieve_valid_field_names(
        self,
        assert_sorted_equal,
        dummy_people_collection,
        api_client,
    ):
        """Ensure retrieve endpoint returns expected data when fields valid."""
        response = api_client.get(
            reverse(
                self.view_name,
                kwargs={
                    'pk': dummy_people_collection.id,
                    'field_names': ('field0',),
                },
            ),
        )
        assert response.status_code == status.HTTP_200_OK
        assert response.data['meta']
        assert_sorted_equal(
            response.data['data'],
            [{'field0': '0', 'count': 3}, {'field0': '1', 'count': 2}],
            key=operator.itemgetter('count', 'field0'),
        )


@pytest.mark.django_db
class TestPeopleCollectionDataListAPIView(object):
    view_name = 'collections:people_data-list'

    def test_get_valid_collection(
        self,
        dummy_people_collection,
        api_client,
    ):
        """Ensure list endpoint returns expected data when collection valid."""
        response = api_client.get(
            reverse(
                self.view_name,
                kwargs={'pk': dummy_people_collection.id},
            ),
            data={'limit': 1},
        )
        assert response.status_code == status.HTTP_200_OK
        assert response.data['meta']
        assert response.data['data'] == [{'field0': '0', 'field1': '10'}]
