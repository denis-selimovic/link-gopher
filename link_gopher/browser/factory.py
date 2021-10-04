from link_gopher.browser.base import BaseBrowser
from link_gopher.browser.firefox.driver import FirefoxBrowser


class BrowserFactory:

    browser_map = {
        'firefox': FirefoxBrowser
    }

    @classmethod
    def get(cls, kind: str) -> BaseBrowser:
        if browser := cls.browser_map.get(kind):
            return browser()

        raise ValueError("Wrong browser type")
