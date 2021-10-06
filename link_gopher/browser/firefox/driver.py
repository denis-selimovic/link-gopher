import time
from typing import Generator, Iterable

from link_gopher.browser.base import BaseBrowser
from link_gopher.browser.firefox.setup import build_driver


class FirefoxBrowser:

    def __init__(self) -> None:
        self.setup_driver()

    def setup_driver(self) -> None:
        self.__driver = build_driver()
        self.__driver.implicitly_wait(5)

    def close(self) -> None:
        self.__driver.close()

    def extract(self, urls: Iterable[str]) -> Generator[str, None, None]:
        for url in urls:
            self.__driver.get(url)

            script = """
                const links = document.querySelectorAll("a").values();
                const hrefs = [];
                for (link of links) {
                    if (/^(http|https):\/\//.test(link)) hrefs.push(link.href);
                }
                return hrefs;
            """
            links = list(set(self.__driver.execute_script(script)))

            for link in links:
                yield url, link

            time.sleep(1)

    def __enter__(self) -> BaseBrowser:
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> bool:
        self.close()
        return True
