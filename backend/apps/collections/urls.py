from django.urls import path

from apps.collections import views

app_name = 'collections'

urlpatterns = [
    path(
        'people/',
        views.PeopleCollectionListCreateAPIView.as_view(),
        name='people-list',
    ),
]
