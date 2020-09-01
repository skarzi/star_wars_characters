import pytest

from rest_framework.request import Request

from apps.collections import (
    models,
    pagination,
)


@pytest.mark.django_db
class TestPeopleCollectionPagination(object):
    @pytest.fixture
    def pagination(self):
        """``PeopleCollectionPagination`` tested instance."""
        return pagination.PeopleCollectionPagination()

    def test_get_paginated_response(self, api_rf, pagination):
        """Ensure `data` keyword is used instead of `results`."""
        pagination.paginate_queryset(
            models.PeopleCollection.objects.none(),
            Request(api_rf.get('/')),
        )
        response = pagination.get_paginated_response([1])
        assert 'results' not in response.data
        assert response.data['data'] == [1]
