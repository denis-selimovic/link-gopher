from abc import abstractmethod
from typing import Generator, Protocol, Tuple


class Output(Protocol):

    @abstractmethod
    def process(self, entires: Generator[Tuple[str, str], None, None],
                dst: str) -> None:
        raise NotImplementedError()
