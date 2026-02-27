from typing import Union, Iterable, Mapping, Any, Optional


NumberLike = Union[int, str]


def to_int(value: NumberLike) -> int:
    if isinstance(value, int):
        return value
    if isinstance(value, str):
        text = value.strip()
        if not text:
            raise ValueError("Empty string cannot be converted to int")
        return int(text, 0)
    raise TypeError(f"Unsupported type for to_int: {type(value)!r}")


def to_float(value: Union[NumberLike, float]) -> float:
    if isinstance(value, float):
        return value
    if isinstance(value, int):
        return float(value)
    if isinstance(value, str):
        text = value.strip()
        if not text:
            raise ValueError("Empty string cannot be converted to float")
        # Попробуем сначала как обычное число, потом как hex
        try:
            return float(text)
        except ValueError:
            return float(int(text, 0))
    raise TypeError(f"Unsupported type for to_float: {type(value)!r}")


def to_bool(value: Any) -> bool:
    if isinstance(value, bool):
        return value
    if isinstance(value, int):
        if value in (0, 1):
            return bool(value)
        raise ValueError(f"Cannot convert int {value!r} to bool (only 0 or 1 allowed)")
    if isinstance(value, str):
        text = value.strip().lower()
        if text in ("", "0", "false", "no", "off"):
            return False
        if text in ("1", "true", "yes", "on"):
            return True
        raise ValueError(f"Cannot convert string {value!r} to bool")
    raise TypeError(f"Unsupported type for to_bool: {type(value)!r}")


def normalize_offset(value: NumberLike) -> int:
    return to_int(value)


def normalize_address(value: NumberLike) -> int:
    addr = to_int(value)
    if addr < 0:
        raise ValueError("Address must be non-negative")
    hex_str = hex(addr)
    return int(hex_str, 16)


def to_hex(value: NumberLike) -> str:
    return hex(to_int(value))


def ensure_positive_int(value: NumberLike, *, allow_zero: bool = False) -> int:
    iv = to_int(value)
    if allow_zero:
        if iv < 0:
            raise ValueError(f"Value must be >= 0, got {iv}")
    else:
        if iv <= 0:
            raise ValueError(f"Value must be > 0, got {iv}")
    return iv


def ensure_in_range(
    value: NumberLike,
    *,
    min_value: Optional[int] = None,
    max_value: Optional[int] = None,
) -> int:
    iv = to_int(value)
    if min_value is not None and iv < min_value:
        raise ValueError(f"Value must be >= {min_value}, got {iv}")
    if max_value is not None and iv > max_value:
        raise ValueError(f"Value must be <= {max_value}, got {iv}")
    return iv


def ensure_non_empty_string(value: Any) -> str:
    if not isinstance(value, str):
        raise TypeError(f"Expected non-empty string, got {type(value)!r}")
    text = value.strip()
    if not text:
        raise ValueError("String must be non-empty")
    return text


def ensure_iterable_not_empty(value: Iterable[Any], *, name: str = "value") -> Iterable[Any]:
    try:
        if len(value) == 0:  # type: ignore[arg-type]
            raise ValueError(f"{name} must not be empty")
        return value
    except TypeError:
        items = list(value)
        if not items:
            raise ValueError(f"{name} must not be empty")
        return items


def ensure_mapping_has_keys(
    mapping: Mapping[str, Any],
    required_keys: Iterable[str],
    *,
    name: str = "mapping",
) -> Mapping[str, Any]:
    """
    Проверка, что в словаре есть все требуемые ключи.
    Удобно для настройки/конфигов.
    """
    missing = [k for k in required_keys if k not in mapping]
    if missing:
        raise KeyError(f"{name} is missing required keys: {', '.join(missing)}")
    return mapping


__all__ = [
    "to_int",
    "to_float",
    "to_bool",
    "normalize_offset",
    "normalize_address",
    "to_hex",
    "ensure_positive_int",
    "ensure_in_range",
    "ensure_non_empty_string",
    "ensure_iterable_not_empty",
    "ensure_mapping_has_keys",
]

