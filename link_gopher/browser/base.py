from abc import abstractmethod
from typing import List, Protocol

from link_gopher.source.base import Source


class BaseBrowser(Protocol):

    @abstractmethod
    def setup_driver(self) -> None:
        raise NotImplementedError()

    @abstractmethod
    def close(self) -> None:
        raise NotImplementedError()

    @abstractmethod
    def extract(self, source: Source) -> List[str]:
        raise NotImplementedError()
