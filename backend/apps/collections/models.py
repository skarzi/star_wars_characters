from django.core.validators import FileExtensionValidator
from django.db import models


class CollectionDownload(models.Model):
    """Model representing Star Wars API people/characters download."""

    file = models.FileField(  # noqa: WPS110
        upload_to='collections/',
        validators=[FileExtensionValidator(allowed_extensions=('csv',))],
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta(object):
        ordering = ('created_at',)

    def __str__(self) -> str:
        """Instance string representation."""
        return '"{0}" <{1}>'.format(
            self.file.path,
            self.created_at.isoformat(timespec='minutes'),
        )
