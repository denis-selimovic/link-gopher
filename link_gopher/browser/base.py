from abc import abstractmethod
from typing import Generator, Iterable, Protocol


class BaseBrowser(Protocol):

    @abstractmethod
    def setup_driver(self) -> None:
        raise NotImplementedError()

    @abstractmethod
    def close(self) -> None:
        raise NotImplementedError()

    @abstractmethod
    def extract(self, urls: Iterable[str]) -> Generator[str, None, None]:
        raise NotImplementedError()
