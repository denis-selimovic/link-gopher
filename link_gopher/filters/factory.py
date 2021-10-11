from typing import List

from link_gopher.filters.base import Filter
from link_gopher.filters.basic.basic_filter import BasicFilter


class FilterFactory:

    filter_map = {
        'basic': BasicFilter
    }

    @classmethod
    def get(cls, kind: str, values: List[str]) -> Filter:
        if filter := cls.filter_map.get(kind):
            return filter(values)

        raise ValueError("Wrong type of filter!")

    @classmethod
    def get_keys(cls):
        return list(cls.filter_map.keys())
