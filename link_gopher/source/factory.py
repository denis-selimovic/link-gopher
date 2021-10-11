from typing import List

from link_gopher.source.base import Source
from link_gopher.source.file.file_source import FileSource
from link_gopher.source.inmemory.inmemory_source import InmemorySource


class SourceFactory:

    source_map = {
        'mem': InmemorySource,
        'txt': FileSource
    }

    @classmethod
    def get(cls, kind: str) -> Source:
        if source := cls.source_map.get(kind):
            return source()

        raise ValueError("Wrong source type")

    @classmethod
    def get_keys(cls) -> List[str]:
        return list(cls.source_map.keys())
