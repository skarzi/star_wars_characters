import pytest

from rest_framework.pagination import LimitOffsetPagination
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

    def test_get_results(self, pagination):
        """Ensure `data` keyword is used instead of `results`."""
        assert pagination.get_results({'data': 1, 'results': 9}) == 1


class TestPETLViewLimitOffsetPagination(object):
    @pytest.fixture
    def pagination(self):
        """``PETLViewLimigOffsetPagination`` tested instance."""
        return pagination.PETLViewLimitOffsetPagination(LimitOffsetPagination())

    @pytest.mark.parametrize(('query_params', 'expected_rows'), [
        ({'offset': 12345}, []),
        ({'offset': 0, 'limit': 1}, [{'field0': '0', 'field1': '10'}]),
        (
            {'offset': 1, 'limit': 2},
            [{'field0': '1', 'field1': '11'}, {'field0': '0', 'field1': '12'}],
        ),
        ({'limit': 4, 'offset': 4}, [{'field0': '0', 'field1': '11'}]),
    ])
    def test_paginate_view(
        self,
        api_rf,
        dummy_petl_view,
        pagination,
        query_params,
        expected_rows,
    ):
        """Ensure properly extracted data are returned."""
        extracted_rows = pagination.paginate_view(
            dummy_petl_view,
            Request(api_rf.get('/', data=query_params)),
        )
        assert extracted_rows == expected_rows

    def test_get_paginated_response(
        self,
        api_rf,
        dummy_petl_view,
        pagination,
    ):
        """Ensure expected ``Response`` object is returned."""
        extracted_rows = pagination.paginate_view(
            dummy_petl_view,
            Request(api_rf.get('/', data={'limit': 3})),
        )
        response = pagination.get_paginated_response(extracted_rows)
        assert len(response.data['results']) == 3
        assert response.data['count'] == 5
        assert response.data['next']
        assert not response.data['previous']
