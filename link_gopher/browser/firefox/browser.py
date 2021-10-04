from link_gopher.browser.firefox.profile import build_driver


class FirefoxBrowser:

    def __init__(self) -> None:
        self.setup_driver()

    def setup_driver(self) -> None:
        self.__driver = build_driver()

    def close(self) -> None:
        pass
