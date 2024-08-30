from typing import type_check_only

def path() -> str: ...

@type_check_only
class _Writer(Protocol):
    def isatty(self) -> bool: ...
    def write(self, content: bytes, /) -> object: ...
    def flush(self) -> object: ...

class ProgressRenderer:
    def __init__(self, stream: _Writer[str], total_count: int) -> None: ...
    def render(self) -> None: ...
    def erase(self) -> None: ...
    def drop(self) -> None: ...
    @property
    def count(self) -> int: ...
    @count.setter
    def count(self, new_count: int) -> None: ...
