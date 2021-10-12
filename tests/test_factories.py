from unittest import TestCase

from link_gopher.browser.factory import BrowserFactory
from link_gopher.browser.firefox.driver import FirefoxBrowser
from link_gopher.filters.basic.basic_filter import BasicFilter
from link_gopher.filters.factory import FilterFactory
from link_gopher.output.factory import OutputFactory
from link_gopher.output.file.file_output import FileOutput
from link_gopher.output.inmemory.inmemory_output import InmemoryOutput
from link_gopher.source.factory import SourceFactory
from link_gopher.source.file.file_source import FileSource
from link_gopher.source.inmemory.inmemory_source import InmemorySource


class SourceFactoryTests(TestCase):

    def test_factory_txt(self):
        source = SourceFactory.get('txt')
        self.assertIs(type(source), FileSource)

    def test_factory_mem(self):
        source = SourceFactory.get('mem')
        self.assertIs(type(source), InmemorySource)

    def test_factory_exception_raised(self):
        self.assertRaises(ValueError, lambda: SourceFactory.get('unknown'))


class OutputFactoryTests(TestCase):

    def test_factory_txt(self):
        output = OutputFactory.get('txt', None)
        self.assertIs(type(output), FileOutput)

    def test_factory_mem(self):
        output = OutputFactory.get('mem', None)
        self.assertIs(type(output), InmemoryOutput)

    def test_factory_exception_raised(self):
        self.assertRaises(
            ValueError, lambda: OutputFactory.get('unknown', None))


class BrowserFactoryTests(TestCase):

    def test_factory_firefox(self):
        browser = BrowserFactory.get('firefox')
        self.assertIs(type(browser), FirefoxBrowser)

    def test_factory_exception_raised(self):
        self.assertRaises(ValueError, lambda: BrowserFactory.get('unknown'))


class FilterFactoryTests(TestCase):

    def test_factory_basic_filter(self):
        filter = FilterFactory.get('basic', [])
        self.assertIs(type(filter), BasicFilter)

    def test_factory_exception_raised(self):
        self.assertRaises(ValueError, lambda: FilterFactory.get('unknown', []))
