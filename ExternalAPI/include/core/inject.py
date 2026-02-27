import pymem
import pymem.process

from .memory import Memory
from .manager import set_default_process


def init(process_name: str = "cs2.exe") -> Memory:
    try:
        proc_entry = pymem.process.process_from_name(process_name)
    except ProcessLookupError:
        raise RuntimeError(f"Process '{process_name}' not found")

    pid = proc_entry.th32ProcessID
    set_default_process(pid)
    return Memory(pid)
