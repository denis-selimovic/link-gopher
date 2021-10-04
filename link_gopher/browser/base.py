from abc import abstractmethod
from typing import Protocol


class BaseBrowser(Protocol):

    @abstractmethod
    def setup_driver(self) -> None:
        raise NotImplementedError()

    @abstractmethod
    def close(self) -> None:
        raise NotImplementedError()
