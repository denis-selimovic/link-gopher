from link_gopher.source.base import Source
from link_gopher.source.file.file_source import FileSource


class SourceFactory:

    source_map = {
        'txt': FileSource
    }

    @classmethod
    def get(cls, kind: str) -> Source:
        if source := cls.source_map.get(kind):
            return source()

        raise ValueError("Wrong source type")
