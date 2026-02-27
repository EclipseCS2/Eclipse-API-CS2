from typing import Optional

from ..Api.manager import ApiManager
from ..validation import normalize_offset
from .manager import CoreManager


def get_offset(name: str, offsets_path: Optional[str] = None) -> int:
    api = ApiManager(offsets_path)
    raw = normalize_offset(api.get_address(name))

    if not (name.startswith("dw") or name in [
        "attack",
        "attack2",
        "back",
        "duck",
        "forward",
        "jump",
        "left",
        "right",
        "use",
        "reload",
        "sprint",
        "lookatweapon",
        "showscores",
        "turnleft",
        "turnright",
        "zoom",
    ]):
        return raw

    core = CoreManager(process=None, offsets_path=offsets_path)

    if name == "dwLocalPlayerPawn":
        ptr_addr = core.get_address(name)          # base + offset (указатель)
        return core.memory.read_longlong(ptr_addr) # адрес pawn

    return core.get_address(name)


class _Parser:
    def __call__(self, target: str, *, offsets_path: Optional[str] = None) -> int:
        return get_offset(target, offsets_path=offsets_path)

    def __getattr__(self, name: str):
        raise AttributeError(
            f"Синтаксис pars.{name}() отключён. Используйте pars('{name}')"
        )


pars = _Parser()

__all__ = ["get_offset", "pars"]

