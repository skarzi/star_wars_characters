from django.urls import (
    path,
    register_converter,
)

from apps.collections import (
    converters,
    views,
)

app_name = 'collections'
register_converter(converters.CSVStringConverter, 'csv_string')
urlpatterns = [
    path(
        'people/',
        views.PeopleCollectionListCreateAPIView.as_view(),
        name='people-list',
    ),
    path(
        'people/<int:pk>/counts/<csv_string:field_names>/',
        views.PeopleCollectionFieldsCountsAPIView.as_view(),
        name='people_fields_counts-detail',
    ),
]
