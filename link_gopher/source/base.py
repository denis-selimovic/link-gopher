from abc import abstractmethod
from typing import Generator, Protocol


class Source(Protocol):

    @abstractmethod
    def get_all(self) -> Generator[str, None, None]:
        raise NotImplementedError()
