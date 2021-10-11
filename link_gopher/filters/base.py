from abc import abstractmethod
from typing import Protocol


class Filter(Protocol):

    @abstractmethod
    def matches(self, link: str) -> bool:
        raise NotImplementedError()
