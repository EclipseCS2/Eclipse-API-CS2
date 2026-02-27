from typing import Optional, Union

from .manager import CoreManager
from ..validation import normalize_address


def set_value(target: Union[int, str], value: int | float, process: int | str | None = None, offsets_path: Optional[str] = None) -> int:
    core = CoreManager(process, offsets_path=offsets_path)

    if isinstance(target, str):
        addr = core.get_address(target)
    else:
        addr = normalize_address(target)

    if isinstance(value, float):
        core.memory.write_float(addr, value)
    else:
        core.memory.write_int(addr, int(value))

    return addr


class _Editor:
    def __call__(
        self,
        target: Union[int, str],
        value: int | float,
        *,
        process: int | str | None = None,
        offsets_path: Optional[str] = None,
    ) -> int:
        return set_value(target, value, process=process, offsets_path=offsets_path)

    def __getattr__(self, name: str):
        raise AttributeError(
            f"Синтаксис edit.{name}(...) отключён. Используйте edit('{name}', ...)"
        )


edit = _Editor()

__all__ = ["set_value", "edit"]
