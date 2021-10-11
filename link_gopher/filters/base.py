from abc import abstractmethod
from typing import List, Protocol


class Filter(Protocol):

    values: List[str]

    @abstractmethod
    def matches(self, link: str) -> bool:
        raise NotImplementedError()
