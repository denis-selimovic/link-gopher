from typing import Generator, Optional, Tuple

from link_gopher.filters.base import Filter


class InmemoryOutput:

    def __init__(self, filter: Optional[Filter]):
        self.filter = filter

    def process(self, entries: Generator[Tuple[str, str], None, None],
                dst: str) -> None:
        for url, link in entries:
            if self.filter is None or self.filter.matches(link):
                print(f'{url} -> {link}')

    def is_valid(self, dst) -> bool:
        return True
