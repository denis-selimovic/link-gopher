from abc import abstractmethod
from typing import Generator, Optional, Protocol, Tuple

from link_gopher.filters.base import Filter


class Output(Protocol):

    filter: Optional[Filter]

    @abstractmethod
    def process(self, entires: Generator[Tuple[str, str], None, None],
                dst: str) -> None:
        raise NotImplementedError()

    @abstractmethod
    def is_valid(self, dst) -> bool:
        raise NotImplementedError()
