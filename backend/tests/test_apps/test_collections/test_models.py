import datetime


def test_collection_download_str_representation(people_collection_factory):
    """Ensure ``PeopleCollection`` has proper string representation."""
    now = datetime.datetime(2020, 8, 30, 10, 54, tzinfo=datetime.timezone.utc)
    collection = people_collection_factory.build(created_at=now)
    assert '<2020-08-30T10:54+00:00>' in str(collection)
    assert 'example.csv"' in str(collection)
