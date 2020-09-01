from rest_framework import (
    generics,
    status,
)
from rest_framework.request import Request
from rest_framework.response import Response

from apps.collections import (
    models,
    pagination,
    serializers,
    services,
)


class PeopleCollectionListCreateAPIView(generics.ListCreateAPIView):
    """``APIView`` to list and create ``PeopleCollection`` instances."""

    pagination_class = pagination.PeopleCollectionPagination
    queryset = models.PeopleCollection.objects.all()
    serializer_class = serializers.PeopleCollectionSerializer

    def create(self, request: Request, *args, **kwargs) -> Response:
        """Create ``PeopleCollection`` instance."""
        collection = services.download_people_collection()
        return Response(
            data={
                'data': self.get_serializer(collection).data,
            },
            status=status.HTTP_201_CREATED,
        )


class PeopleCollectionFieldsCountsAPIView(generics.RetrieveAPIView):
    """``APIView`` to count ``PeopleCollection`` fields combinations."""

    queryset = models.PeopleCollection.objects.all()

    def retrieve(self, request: Request, *args, **kwargs) -> Response:
        """Count combinations of all fields values in requested collection."""
        collection = self.get_object()
        return Response(
            data={
                'data': services.count_fields(
                    collection.petl_view,
                    kwargs['field_names'],
                ),
            },
            status=status.HTTP_200_OK,
        )
