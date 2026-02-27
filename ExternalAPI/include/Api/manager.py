from typing import Optional

from .parser import get_address_by_name


class ApiManager:

    def __init__(self, offsets_path: Optional[str] = None) -> None:
        self._offsets_path = offsets_path

    def get_address(self, name: str) -> int:
        return get_address_by_name(name, self._offsets_path)
