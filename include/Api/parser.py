import requests
from pathlib import Path
from typing import Dict, Tuple, Optional

GITHUB_USER = "EclipseCS2"
REPO_NAME = "ExternalAPI"
RAW_URL = f"https://raw.githubusercontent.com/EclipseCS2/ExternalAPI/refs/heads/main/ExternalAPI/offsets.cfg"

def _default_offsets_path() -> Path:
    """Определяет путь к файлу offsets.cfg в корне проекта."""
    return Path(__file__).resolve().parents[2] / "offsets.cfg"

def download_offsets(path: Path) -> bool:
    """
    Скачивает свежий файл офсетов с GitHub и сохраняет его локально.
    """
    try:
        print(f"[API] Checking for updates at: {RAW_URL}")
        response = requests.get(RAW_URL, timeout=10)
        if response.status_code == 200:
            path.write_text(response.text, encoding="utf-8")
            print(f"[API] Success! Offsets saved to {path.name}")
            return True
        else:
            print(f"[API] Failed to download: Status {response.status_code}")
            return False
    except Exception as e:
        print(f"[API] Network error during update: {e}")
        return False

def parse_offsets(path: str | None = None) -> Dict[str, int]:
    """Парсит файл офсетов и возвращает словарь {имя: адрес}."""
    cfg_path = Path(path) if path is not None else _default_offsets_path()
    offsets: Dict[str, int] = {}

    if not cfg_path.is_file():
        if not download_offsets(cfg_path):
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
            addr = int(value, 0)
            offsets[name] = addr
        except ValueError:
            continue

    return offsets

def parse_offsets_with_modules(path: str | None = None) -> Dict[str, Tuple[int, Optional[str]]]:
    """Парсит офсеты и привязывает их к модулям (DLL)."""
    cfg_path = Path(path) if path is not None else _default_offsets_path()
    result: Dict[str, Tuple[int, Optional[str]]] = {}
    current_module: Optional[str] = None

    if not cfg_path.is_file():
        if not download_offsets(cfg_path):
            return result

    text = cfg_path.read_text(encoding="utf-8", errors="ignore")
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line:
            continue

        if line.startswith("#"):
            # Извлекаем имя модуля из комментария, например: "# client.dll"
            potential_module = line.lstrip("#").strip()
            if potential_module.lower().endswith(".dll"):
                current_module = potential_module
            continue

        if "=" not in line:
            continue

        name, value = line.split("=", 1)
        name = name.strip()
        value = value.strip().strip("'\"")

        try:
            addr = int(value, 0)
            result[name] = (addr, current_module)
        except ValueError:
            continue

    return result

def get_address_by_name(name: str, path: str | None = None) -> int:
    """Возвращает адрес по его имени. Выбрасывает ошибку, если имя не найдено."""
    offsets = parse_offsets(path)
    if name not in offsets:
        raise KeyError(f"Offset '{name}' not found in offsets.cfg")
    return offsets[name]

def get_address_and_module(name: str, path: str | None = None) -> Tuple[int, Optional[str]]:
    """Возвращает кортеж (адрес, имя_модуля) по имени офсета."""
    offsets = parse_offsets_with_modules(path)
    if name not in offsets:
        raise KeyError(f"Offset '{name}' not found in offsets.cfg")
    return offsets[name]