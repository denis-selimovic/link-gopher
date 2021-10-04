from link_gopher.output.base import Output
from link_gopher.output.file.file_output import FileOutput


class OutputFactory:

    output_map = {
        'txt': FileOutput
    }

    @classmethod
    def get(cls, kind: str) -> Output:
        if output := cls.output_map.get(kind):
            return output()

        raise ValueError("Wrong type of output")
