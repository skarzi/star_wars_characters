import pytest

from apps.collections import serializers


@pytest.mark.django_db
class TestPeopleCollectionDataMetaSerializer(object):
    def test_get_filename(self, people_collection):
        """Ensure proper filename is returned."""
        serializer = serializers.PeopleCollectionDataMetaSerializer()
        assert 'example' in serializer.get_filename(people_collection)
