from typing import (
    Any,
    Dict,
    List,
)

import petl

from rest_framework import pagination
from rest_framework.request import Request
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

    def get_results(self, data: Dict[str, Any]) -> Any:  # noqa: WPS110
        """Use `data` keyword instead of `results`."""
        return data['data']


class PETLViewLimitOffsetPagination(object):
    """`PETL` view/table custom pagination."""

    def __init__(
        self,
        drf_pagination: pagination.LimitOffsetPagination,
    ) -> None:
        """Set regular `rest_framework` pagination."""
        self.drf_pagination = drf_pagination

    def paginate_view(
        self,
        petl_view: petl.Table,
        request: Request,
        **kwargs,
    ) -> List[Any]:
        """Paginate ``petl_view`` based on data extracted from ``request``."""
        self._set_attributes(petl_view, request)
        if self.count == 0 or self.offset > self.count:
            return []
        rows_iterator = iter(
            petl_view.rowslice(self.offset, self.offset + self.limit),
        )
        keys = next(rows_iterator, ())
        return [dict(zip(keys, row)) for row in rows_iterator]

    def get_paginated_response(
        self,
        data: List[Any],  # noqa: WPS110
    ) -> Response:
        """Proxy call to ``drf_pagination``."""
        return self.drf_pagination.get_paginated_response(data)

    def _set_attributes(self, petl_view: petl.Table, request: Request) -> None:
        self.count = petl_view.nrows()
        self.drf_pagination.count = self.count
        self.limit = self.drf_pagination.get_limit(request) or self.count
        self.drf_pagination.limit = self.limit
        self.offset = self.drf_pagination.get_offset(request)
        self.drf_pagination.offset = self.offset
        self.drf_pagination.request = request
