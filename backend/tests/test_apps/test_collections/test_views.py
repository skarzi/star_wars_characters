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
