from abc import abstractmethod
from typing import Generator, Protocol, Tuple


class Output(Protocol):

    @abstractmethod
    def process(self, entires: Generator[Tuple[str, str], None, None],
                dst: str) -> None:
        raise NotImplementedError()

    @abstractmethod
    def is_valid(self, dst) -> bool:
        raise NotImplementedError()
