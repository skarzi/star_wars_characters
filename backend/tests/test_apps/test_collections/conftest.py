from django.core.files.base import ContentFile

import petl
import pytest


@pytest.fixture
def dummy_csv_content():
    """Bytes with dummy CSV data."""
    return b'field0,field1\n0,10\n1,11\n0,12\n1,10\n0,11'


@pytest.fixture
def dummy_petl_view(dummy_csv_content):
    """``petl`` view with dummy CSV data."""
    return petl.fromcsv(petl.io.MemorySource(dummy_csv_content))


@pytest.fixture
def dummy_people_collection(people_collection_factory, dummy_csv_content):
    """``PeopleCollection`` dummy instance used in tests."""
    return people_collection_factory.create(
        file=ContentFile(dummy_csv_content, name='dummy_test.csv'),
    )
