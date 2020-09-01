import factory


class PeopleCollectionFactory(factory.django.DjangoModelFactory):
    file = factory.django.FileField(filename='example.csv')  # noqa: WPS110

    class Meta(object):
        model = 'collections.PeopleCollection'
