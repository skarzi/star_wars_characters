import datetime


def test_collection_download_str_representation(collection_download_factory):
    """Ensure ``CollectionDownload`` has proper string representation."""
    now = datetime.datetime(2020, 8, 30, 10, 54, tzinfo=datetime.timezone.utc)
    collection_download = collection_download_factory.build(created_at=now)
    assert '<2020-08-30T10:54+00:00>' in str(collection_download)
    assert 'example.csv"' in str(collection_download)
