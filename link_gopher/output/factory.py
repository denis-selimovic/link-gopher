from typing import List

from link_gopher.output.base import Output
from link_gopher.output.file.file_output import FileOutput
from link_gopher.output.inmemory.inmemory_output import InmemoryOutput


class OutputFactory:

    output_map = {
        'mem': InmemoryOutput,
        'txt': FileOutput
    }

    @classmethod
    def get(cls, kind: str) -> Output:
        if output := cls.output_map.get(kind):
            return output()

        raise ValueError("Wrong type of output")

    @classmethod
    def get_keys(cls) -> List[str]:
        return list(cls.output_map.keys())
