from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils.functional import cached_property

import petl


class PeopleCollection(models.Model):
    """Model representing Star Wars API people/characters download."""

    file = models.FileField(  # noqa: WPS110
        upload_to='collections/people/%Y/%m/%d/',  # noqa: WPS323
        validators=[FileExtensionValidator(allowed_extensions=('csv',))],
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta(object):
        ordering = ('-created_at',)

    def __str__(self) -> str:
        """Instance's string representation."""
        return '"{0}" <{1}>'.format(
            self.file.path,
            self.created_at.isoformat(timespec='minutes'),
        )

    @cached_property
    def petl_view(self) -> petl.Table:
        """``petl.Table`` built from stored CSV ``file``."""
        return petl.fromcsv(source=self.file)
