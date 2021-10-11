from typing import Generator


class InmemorySource:

    def get_all(self, source: str) -> Generator[str, None, None]:
        for row in source.split(","):
            yield row.strip()
