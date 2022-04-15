import random


def get_random_bool():
    """ Gets a random boolean.

    Example usage:
        get_random_bool() -> [ True | False ]
    """

    return bool(random.getrandbits(1))
