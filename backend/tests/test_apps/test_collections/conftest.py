from django.core.files.base import ContentFile

import pytest


@pytest.fixture
def dummy_people_collection(people_collection_factory):
    """``PeopleCollection`` dummy instance used in tests."""
    dummy_content = b'field0,field1\n0,10\n1,11\n0,12\n1,10\n0,11'
    return people_collection_factory.create(
        file=ContentFile(dummy_content, name='dummy_test.csv'),
    )
