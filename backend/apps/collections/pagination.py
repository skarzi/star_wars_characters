from typing import (
    Any,
    List,
)

from rest_framework import pagination
from rest_framework.response import Response


class PeopleCollectionPagination(pagination.LimitOffsetPagination):
    """``PeopleCollection`` custom pagination."""

    default_limit: int = 10
    max_limit: int = default_limit

    # TODO: override also ``get_paginated_response_schema``
    def get_paginated_response(
        self,
        data: List[Any],  # noqa: WPS110
    ) -> Response:
        """Use `data` keyword instead of `results`."""
        response = super().get_paginated_response(data)
        response.data['data'] = response.data.pop('results', [])  # type: ignore
        return response
