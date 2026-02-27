from typing import Optional

from ..Api.manager import ApiManager
from ..Api.parser import get_address_and_module
from .memory import Memory


_default_process: int | str | None = None


def set_default_process(process: int | str) -> None:
    global _default_process
    _default_process = process


def get_default_process() -> int | str:
    if _default_process is None:
        raise RuntimeError("Default process is not set.")
    return _default_process


class CoreManager:
    def __init__(self, process: int | str | None = None, offsets_path: Optional[str] = None) -> None:
        if process is None:
            process = get_default_process()

        self.api_manager = ApiManager(offsets_path)
        self._offsets_path = offsets_path
        self.memory = Memory(process)

    def get_address(self, name: str) -> int:
        offset = self.api_manager.get_address(name)

        needs_base = name.startswith("dw") or name in [
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
        ]

        if not needs_base:
            return offset

        _, module_name = get_address_and_module(name, self._offsets_path)
        dll_name = module_name or "client.dll"

        base = self.memory.get_module_base(dll_name)
        return base + offset
