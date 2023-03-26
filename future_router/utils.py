"""Utility"""
from typing import Any, Iterable


def multiple_hasattr(obj, items: Iterable[str]):
    """Does a class/object has specific items?"""
    return all((hasattr(obj, item) for item in items))


class FrozenDict(dict):
    """Frozen Dict"""

    def __init__(self, *args, **kwargs):
        setattr(self, '_closed', False)
        super().__init__(*args, **kwargs)
        setattr(self, '_closed', True)

    def __setattr__(self, __name: str, __value: Any) -> None:
        if not getattr(self, '_closed', True):
            return super().__setattr__(__name, __value)
        return None

class AttrDict(dict):
    """Attribute Dictionary"""

    def __getattr__(self, __name: str) -> Any:
        try:
            return super().__getattribute__(__name)
        except AttributeError:
            return self[__name]
