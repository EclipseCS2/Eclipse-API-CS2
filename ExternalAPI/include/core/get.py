from typing import Optional, Union

from .manager import CoreManager
from ..validation import normalize_address


def get_value(target: Union[int, str], process: int | str | None = None, as_float: bool = False, offsets_path: Optional[str] = None) -> int | float:
    core = CoreManager(process, offsets_path=offsets_path)

    if isinstance(target, str):
        addr = core.get_address(target)
    else:
        addr = normalize_address(target)

    if as_float:
        return core.memory.read_float(addr)
    return core.memory.read_int(addr)


class _Getter:
    def __call__(
        self,
        target: Union[int, str],
        *,
        process: int | str | None = None,
        as_float: bool = False,
        offsets_path: Optional[str] = None,
    ) -> int | float:
        return get_value(target, process=process, as_float=as_float, offsets_path=offsets_path)

    def __getattr__(self, name: str):
        raise AttributeError(
            f"Синтаксис get.{name}() отключён. Используйте get('{name}')"
        )


get = _Getter()

__all__ = ["get_value", "get"]
