from abc import abstractmethod
from typing import List, Protocol


class Source(Protocol):

    @abstractmethod
    def get_all() -> List[str]:
        raise NotImplementedError()
