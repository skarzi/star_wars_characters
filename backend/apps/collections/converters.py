from typing import (
    ClassVar,
    Sequence,
    Tuple,
)


class CSVStringConverter(object):
    """Plain CSV formatted string converter."""

    regex: ClassVar[str] = r'(?:[^/,]+,?)+'

    def to_python(self, value: str) -> Tuple[str, ...]:  # noqa: WPS110
        """Convert raw CSV string value to Python primitive object."""
        return tuple(
            cleaned_item for raw_item in value.split(',')
            if (cleaned_item := raw_item.strip())
        )

    def to_url(self, value: Sequence[str]) -> str:  # noqa: WPS110
        """Convert Python primitive object to CSV formatted string."""
        return ','.join(value)
