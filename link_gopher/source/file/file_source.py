from typing import Generator


class FileSource:

    def __init__(self, file) -> None:
        self.__file = file

    def get_all(self) -> Generator[str, None, None]:
        with open(self.__file, 'r') as file:
            for line in file:
                yield line.strip()
