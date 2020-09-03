from pathlib import Path

from rest_framework import serializers

from apps.collections import models


class PeopleCollectionSerializer(serializers.ModelSerializer):
    """``PeopleCollection`` read-only serializer."""

    class Meta(object):
        model = models.PeopleCollection
        fields = ('id', 'created_at', 'file')
        read_only_fields = fields


class PeopleCollectionDataMetaSerializer(PeopleCollectionSerializer):
    """``PeopleCollection`` read-only serializer used in meta namespace."""

    filename = serializers.SerializerMethodField()

    class Meta(PeopleCollectionSerializer.Meta):
        fields = ('created_at', 'file', 'filename')

    def get_filename(self, instance: models.PeopleCollection) -> str:
        """Extract filename from full path."""
        return Path(getattr(instance.file, 'name', '') or '').name
