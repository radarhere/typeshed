from collections.abc import Callable

from .import_hook import instrument_imports

def Setup(
    args: list[str],
    test_one_input: Callable[[bytes], None],
    **kwargs: bool | Callable[[bytes, int, int], str | bytes] | Callable[[bytes, bytes, int, int], str | bytes] | None,
) -> list[str]: ...
def Fuzz() -> None: ...
def Mutate(data: bytes, max_size: int) -> bytes: ...
