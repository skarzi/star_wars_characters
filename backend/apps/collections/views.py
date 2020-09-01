import petl

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
        """Count all combination of all field names."""
        collection = self.get_object()
        # TODO: add ``field_names`` validation
        field_names = kwargs['field_names']
        fields_counts = petl.valuecounts(collection.petl_view, *field_names)
        fields_counts = fields_counts.cutout('frequency')
        fields_counts_iterator = iter(fields_counts)
        keys = next(fields_counts_iterator, [])
        return Response(
            data={
                'data': [
                    dict(zip(keys, row)) for row in fields_counts_iterator
                ],
            },
            status=status.HTTP_200_OK,
        )
