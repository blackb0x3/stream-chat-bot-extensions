from typing import Any
import builtins
import random


def get_random_bool():
    """ Gets a random boolean.

    Example usage:
        get_random_bool() -> [ True | False ]
    """

    return bool(random.getrandbits(1))


def igetattr(obj: object, name: str, /) -> Any:
    """ Case-insensitive getattr() call.

    Example usage:
        igetattr(obj, name) -> Any
    """
    for a in dir(obj):
        if a.lower() == name.lower():
            return builtins.getattr(obj, a)
