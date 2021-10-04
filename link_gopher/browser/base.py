from abc import abstractmethod
from typing import Iterable, List, Protocol


class BaseBrowser(Protocol):

    @abstractmethod
    def setup_driver(self) -> None:
        raise NotImplementedError()

    @abstractmethod
    def close(self) -> None:
        raise NotImplementedError()

    @abstractmethod
    def extract(self, urls: Iterable[str]) -> List[str]:
        raise NotImplementedError()
