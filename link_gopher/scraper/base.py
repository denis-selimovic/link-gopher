from typing import List, Optional

from link_gopher.browser.base import BaseBrowser
from link_gopher.browser.factory import BrowserFactory
from link_gopher.filters.base import Filter
from link_gopher.filters.factory import FilterFactory
from link_gopher.output.base import Output
from link_gopher.output.factory import OutputFactory
from link_gopher.source.base import Source
from link_gopher.source.factory import SourceFactory


class Scraper:

    def __init__(self, browser: str, source: str, dst: str,
                 filter: str, values: List[str]) -> None:
        self.__browser: BaseBrowser = BrowserFactory.get(browser)
        self.__source: Source = SourceFactory.get(source)
        self.__filter: Optional[Filter] = FilterFactory.get(
            filter, values) if filter else None
        self.__output: Output = OutputFactory.get(dst, self.__filter)

    def load(self, input: str, output: str) -> None:
        urls = self.__source.get_all(input)

        with self.__browser as browser:
            links = browser.extract(urls)
            self.__output.process(links, output)
