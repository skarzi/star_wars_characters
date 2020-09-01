import re

import pytest

from apps.collections import converters


class TestCSVStringConverter(object):
    @pytest.fixture
    def converter(self):
        """``CSVStringConverter`` used in tests."""
        return converters.CSVStringConverter()

    @pytest.mark.parametrize(('string', 'match_result'), [
        ('', False),
        ('/', False),
        ('a', True),
        ('a,b', True),
        ('a, b,c', True),
    ])
    def test_regex(self, converter, string, match_result):
        """Ensure ``regex`` matches expected values."""
        assert bool(re.match(converter.regex, string)) is match_result

    @pytest.mark.parametrize(('input_string', 'expected_result'), [
        ('a', ('a',)),
        ('a,', ('a',)),
        ('   a,', ('a',)),
        ('   a   ,', ('a',)),
        ('a,b', ('a', 'b')),
        ('a, b, c', ('a', 'b', 'c')),
    ])
    def test_to_python(self, converter, input_string, expected_result):
        """Ensure properly striped and expected values are returned."""
        assert converter.to_python(input_string) == expected_result

    @pytest.mark.parametrize(('input_value', 'expected_url'), [
        ((), ''),
        (('a',), 'a'),
        (('a', 'b', 'c'), 'a,b,c'),
    ])
    def test_to_url(self, converter, input_value, expected_url):
        """Ensure properly striped and expected values are returned."""
        assert converter.to_url(input_value) == expected_url
