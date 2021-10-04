from link_gopher.browser.base import BaseBrowser
from link_gopher.browser.factory import BrowserFactory
from link_gopher.source.base import Source
from link_gopher.source.factory import SourceFactory


class Scraper:

    def __init__(self, browser: str, source: str) -> None:
        self.__browser: BaseBrowser = BrowserFactory.get(browser)
        self.__source: Source = SourceFactory.get(source)

    def load(self, input: str) -> None:
        urls = self.__source.extract_all(input)

        with self.__browser as browser:
            links = browser.extract(urls)

        for link in links:
            print(link)


if __name__ == 'main':
    s = Scraper('firefox', 'txt')
    s.load('test.txt')
