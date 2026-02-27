import pymem
import pymem.process


class Memory:

    def __init__(self, process: int | str) -> None:
        if isinstance(process, int):
            pm = pymem.Pymem()
            pm.open_process_from_id(process)
        else:
            pm = pymem.Pymem(process)

        self._pm = pm

    def get_module_base(self, module_name: str) -> int:
        module = pymem.process.module_from_name(self._pm.process_handle, module_name)
        if not module:
            return 0
        return module.lpBaseOfDll

    # --- указатели (8 байт, x64) ---
    def read_longlong(self, address: int) -> int:
        return self._pm.read_longlong(address)

    # --- базовые байты ---
    def read_bytes(self, address: int, size: int) -> bytes:
        return self._pm.read_bytes(address, size)

    def write_bytes(self, address: int, data: bytes | bytearray) -> None:
        self._pm.write_bytes(address, data)

    # --- int (4 байта) ---
    def read_int(self, address: int) -> int:
        return self._pm.read_int(address)

    def write_int(self, address: int, value: int) -> None:
        self._pm.write_int(address, int(value))

    # --- float (4 байта) ---
    def read_float(self, address: int) -> float:
        return self._pm.read_float(address)

    def write_float(self, address: int, value: float) -> None:
        self._pm.write_float(address, float(value))

    # --- double (8 байт) ---
    def read_double(self, address: int) -> float:
        return self._pm.read_double(address)

    def write_double(self, address: int, value: float) -> None:
        self._pm.write_double(address, float(value))

    def close(self) -> None:
        self._pm.close_process()
