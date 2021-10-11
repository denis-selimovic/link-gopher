from typing import Generator, Tuple


class InmemoryOutput:

    def process(self, entries: Generator[Tuple[str, str], None, None],
                dst: str) -> None:
        for url, link in entries:
            print(f'{url} -> {link}')
