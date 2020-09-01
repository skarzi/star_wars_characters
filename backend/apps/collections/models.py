from django.core.validators import FileExtensionValidator
from django.db import models


# NOTE: potential `mypy` bug:
# https://github.com/typeddjango/django-stubs/issues/142
class PeopleCollection(models.Model):  # type: ignore[misc]
    """Model representing Star Wars API people/characters download."""

    file = models.FileField(  # noqa: WPS110
        upload_to='collections/people/%Y/%m/%d/',  # noqa: WPS323
        validators=[FileExtensionValidator(allowed_extensions=('csv',))],
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta(object):
        ordering = ('created_at',)

    def __str__(self) -> str:
        """Instance's string representation."""
        return '"{0}" <{1}>'.format(
            self.file.path,
            self.created_at.isoformat(timespec='minutes'),
        )
