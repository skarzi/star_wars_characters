from typing import (
    ClassVar,
    Iterator,
    Tuple,
)

from django.conf import settings

import petl

from requests import Response

from apps.star_wars_api.client import StarWarsAPIClient
from apps.star_wars_api.urls import url_join


class BaseCollectionView(petl.Table):
    """Star Wars API resource collection view/iterator."""

    collection_name: str
    field_names: ClassVar[Tuple[str, ...]]

    def __init__(self, client: StarWarsAPIClient) -> None:
        """Initialize ``CollectionView`` instance."""
        self.client = client

    def __iter__(self) -> Iterator[Tuple[str, ...]]:
        """Iterate over Star Wars API resource collection."""
        yield tuple(self.field_names)
        initial_response = self.client.get(self.url)
        for response in self.client.follow_pagination(initial_response):
            yield from self.process(response)

    @property
    def url(self) -> str:
        """URL of collection named with ``collection_name``."""
        return url_join(settings.STAR_WARS_API_URL, self.collection_name)

    def process(self, response: Response) -> Iterator[Tuple[str, ...]]:
        """Process Star Wars API resource collection response to PETL row."""
        yield from (
            tuple(resource[name] for name in self.field_names)
            for resource in response.json().get('results', [])
        )


class PeopleCollectionView(BaseCollectionView):
    """Star Wars API people collection view/iterator."""

    collection_name = 'people'
    field_names: ClassVar[Tuple[str, ...]] = (
        'url',
        'name',
        'height',
        'mass',
        'hair_color',
        'skin_color',
        'eye_color',
        'birth_year',
        'gender',
        # fields necessary to properly perform post processing
        'homeworld',
        'edited',
    )


class PlanetsCollectionView(BaseCollectionView):
    """Star Wars API planets collection view/iterator."""

    collection_name = 'planets'
    field_names: ClassVar[Tuple[str, ...]] = ('url', 'name')


def process_people_collection_view(
    people_view: PeopleCollectionView,
    planets_view: PlanetsCollectionView,
) -> petl.Table:
    """Process Star Wars API people collection.

    Resolves `homeworld` field, adds `date` field, drops `edited` field.

    """
    iso_parser = petl.util.parsers.datetimeparser(
        '%Y-%m-%dT%H:%M:%S.%f%z',  # noqa: WPS323
    )
    homeworld_key = 'homeworld'
    # TODO: consider using ``hashleftjoin``
    people_view = people_view.leftjoin(
        planets_view,
        lkey=homeworld_key,
        rkey='url',
        rprefix='homeworld_',
    )
    people_view = people_view.cutout(homeworld_key)
    people_view = people_view.rename('homeworld_name', homeworld_key)
    people_view = people_view.addfield(
        'date',
        (
            lambda row: iso_parser(row['edited']).strftime('%Y-%m-%d')  # noqa: E501, WPS323
        ),
    )
    return people_view.cutout('edited')
