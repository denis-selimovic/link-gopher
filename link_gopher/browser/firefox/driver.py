from link_gopher.browser.base import BaseBrowser
from link_gopher.browser.firefox.setup import build_driver


class FirefoxBrowser:

    def __init__(self) -> None:
        self.setup_driver()

    def setup_driver(self) -> None:
        self.__driver = build_driver()

    def close(self) -> None:
        self.__driver.close()

    def __enter__(self) -> BaseBrowser:
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> bool:
        self.close()
        return True
