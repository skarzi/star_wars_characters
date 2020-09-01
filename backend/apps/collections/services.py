import uuid

from typing import (
    Any,
    Dict,
    List,
    Optional,
    Tuple,
)

from django.core.files.base import ContentFile

import petl

from petl.io.sources import MemorySource

from apps.collections.models import PeopleCollection
from apps.star_wars_api import petl_views
from apps.star_wars_api.client import StarWarsAPIClient


def download_people_collection(
    client: Optional[StarWarsAPIClient] = None,
) -> PeopleCollection:
    """Download Star Wars API people collection and saves it in DB."""
    client = client or StarWarsAPIClient()
    people_view = petl_views.process_people_collection_view(
        petl_views.PeopleCollectionView(client),
        petl_views.PlanetsCollectionView(client),
    )
    people_view_output = MemorySource()
    people_view.tocsv(people_view_output)

    instance = PeopleCollection()
    instance.file.save(
        '{0}.csv'.format(uuid.uuid4().hex),
        ContentFile(people_view_output.getvalue()),
    )
    return instance


def count_fields(
    petl_view: petl.Table,
    field_names: Tuple[str, ...],
) -> List[Dict[str, Any]]:
    """Count combinations of ``field_names`` fields in given ``petl_view``."""
    # TODO: add ``field_names`` validation
    fields_counts = petl.valuecounts(petl_view, *field_names)
    fields_counts = fields_counts.cut(*field_names, 'count')
    fields_counts_iterator = iter(fields_counts)
    keys: Tuple[str, ...] = next(fields_counts_iterator, ())
    return [
        dict(zip(keys, row)) for row in fields_counts_iterator
    ]
