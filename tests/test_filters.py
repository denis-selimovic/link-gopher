from unittest import TestCase

from link_gopher.filters.factory import FilterFactory


class BasicFilterTests(TestCase):

    def test_basic_filters_one_match(self):
        filter = FilterFactory.get('basic', ['python', 'github', 'facebook'])
        self.assertTrue(filter.matches('https://python.org'))

    def test_basic_filter_multiple_matches(self):
        filter = FilterFactory.get('basic', ['python', 'github', 'py'])
        self.assertTrue(filter.matches('https://python.org'))

    def test_basic_filter_no_match(self):
        filter = FilterFactory.get('basic', ['python', 'github', 'facebook'])
        self.assertFalse(filter.matches('https://google.com'))

    def test_basic_filter_empty_values(self):
        filter = FilterFactory.get('basic', [])
        self.assertFalse(filter.matches('https://python.org'))
