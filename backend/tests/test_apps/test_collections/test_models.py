import datetime

import petl
import pytest


def test_people_collection_str_representation(people_collection_factory):
    """Ensure ``PeopleCollection`` has proper string representation."""
    now = datetime.datetime(2020, 8, 30, 10, 54, tzinfo=datetime.timezone.utc)
    collection = people_collection_factory.build(created_at=now)
    assert '<2020-08-30T10:54+00:00>' in str(collection)
    assert 'example.csv"' in str(collection)


@pytest.mark.django_db
def test_people_collection_petl_view(tmp_path, dummy_people_collection):
    """Ensure valid ``petl.Table`` instance is returned."""
    assert isinstance(dummy_people_collection.petl_view, petl.Table)
    assert dummy_people_collection.petl_view.nrows() == 5
