from rest_framework import (
    generics,
    status,
)
from rest_framework.request import Request
from rest_framework.response import Response

from apps.collections import (
    models,
    serializers,
    services,
)


class PeopleCollectionListCreateAPIView(generics.ListCreateAPIView):
    """``APIView`` to list and create ``PeopleCollection`` instances."""

    queryset = models.PeopleCollection.objects.all()

    def create(self, request: Request, *args, **kwargs) -> Response:
        """Create ``PeopleCollection`` instance."""
        collection = services.download_people_collection()
        return Response(
            data={
                'data': serializers.PeopleCollectionSerializer(collection).data,
            },
            status=status.HTTP_201_CREATED,
        )
