from rest_framework import serializers

from apps.collections import models


class PeopleCollectionSerializer(serializers.ModelSerializer):
    """``PeopleCollection`` read-only serializer."""

    class Meta(object):
        model = models.PeopleCollection
        fields = ('id', 'created_at', 'file')
        read_only_fields = fields
