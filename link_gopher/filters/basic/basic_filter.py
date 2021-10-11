from typing import List


class BasicFilter:

    def __init__(self, values: List[str]) -> None:
        self.values = values

    def matches(self, link: str) -> bool:
        return any([v in link for v in self.values])
