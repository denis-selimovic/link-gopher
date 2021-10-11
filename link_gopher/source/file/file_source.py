import os
from typing import Generator


class FileSource:

    def get_all(self, source: str) -> Generator[str, None, None]:
        with open(source, 'r') as file:
            for line in file:
                yield line.strip("\n")

    def is_valid(self, src) -> bool:
        return os.path.exists(src) if src is not None else False
