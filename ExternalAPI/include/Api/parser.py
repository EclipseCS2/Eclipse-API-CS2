from pathlib import Path
from typing import Dict, Tuple, Optional


def _default_offsets_path() -> Path:
    return Path(__file__).resolve().parents[2] / "offsets.cfg"


def parse_offsets(path: str | None = None) -> Dict[str, int]:
    cfg_path = Path(path) if path is not None else _default_offsets_path()
    offsets: Dict[str, int] = {}

    if not cfg_path.is_file():
        return offsets

    text = cfg_path.read_text(encoding="utf-8", errors="ignore")
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue

        if "=" not in line:
            continue

        name, value = line.split("=", 1)
        name = name.strip()
        value = value.strip().strip("'\"")

        if not name or not value:
            continue

        try:
            # int(..., 0) понимает и 0xHEX, и обычные числа
            addr = int(value, 0)
        except ValueError:
            continue

        offsets[name] = addr

    return offsets


def parse_offsets_with_modules(path: str | None = None) -> Dict[str, Tuple[int, Optional[str]]]:
    cfg_path = Path(path) if path is not None else _default_offsets_path()
    result: Dict[str, Tuple[int, Optional[str]]] = {}
    current_module: Optional[str] = None

    if not cfg_path.is_file():
        return result

    text = cfg_path.read_text(encoding="utf-8", errors="ignore")
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line:
            continue

        if line.startswith("#"):
            # Пытаемся вытащить название DLL: "# client.dll"
            name = line.lstrip("#").strip()
            current_module = name or None
            continue

        if "=" not in line:
            continue

        name, value = line.split("=", 1)
        name = name.strip()
        value = value.strip().strip("'\"")

        if not name or not value:
            continue

        try:
            addr = int(value, 0)
        except ValueError:
            continue

        result[name] = (addr, current_module)

    return result


def get_address_by_name(name: str, path: str | None = None) -> int:
    offsets = parse_offsets(path)
    if name not in offsets:
        raise KeyError(f"Offset '{name}' not found in offsets.cfg")
    return offsets[name]


def get_address_and_module(name: str, path: str | None = None) -> Tuple[int, Optional[str]]:
    offsets = parse_offsets_with_modules(path)
    if name not in offsets:
        raise KeyError(f"Offset '{name}' not found in offsets.cfg")
    return offsets[name]
