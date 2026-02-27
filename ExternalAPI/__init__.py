from .include.core import inject
from .include.core.get import get
from .include.core.edit import edit
from .include.core.pars import pars


def init(process_name: str = "cs2.exe"):
    return inject.init(process_name)


__all__ = ["init", "inject", "get", "edit", "pars"]
