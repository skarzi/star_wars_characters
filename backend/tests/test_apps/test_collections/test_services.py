import petl
import pytest

from apps.collections import services


@pytest.mark.django_db
def test_download_people_collection(mocker, client):
    """Ensure proper ``CollectionDownload`` instance is created."""
    mocker.patch(
        'apps.star_wars_api.petl_views.process_people_collection_view',
        return_value=petl.fromdicts(
            dicts=[{'id': 1, 'name': 'Name 1'}, {'id': 2, 'name': 'Name 2'}],
            header=('id', 'name'),
        ),
    )
    instance = services.download_people_collection(client)
    with instance.file.open(mode='r') as csv_file:
        assert csv_file.read() == 'id,name\n1,Name 1\n2,Name 2\n'
