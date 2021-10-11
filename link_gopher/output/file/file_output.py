from typing import Generator, Tuple


class FileOutput:

    def process(self, entries: Generator[Tuple[str, str], None, None],
                dst: str) -> None:
        with open(dst, 'w+') as file:
            for url, link in entries:
                file.write(f'{url} -> {link}\n')

    def is_valid(self, dst) -> bool:
        return True
