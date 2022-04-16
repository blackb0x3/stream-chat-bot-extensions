import numpy as np

DEFAULT_MIN = 1
DEFAULT_MAX = 6
DEFAULT_TIMES_TO_ROLL = 1


class Dice(object):
    def __init__(self) -> None:
        pass

    async def roll(self, **kwargs):
        dice_min = int(kwargs.get('min', DEFAULT_MIN))
        dice_max = int(kwargs.get('max', DEFAULT_MAX))
        times_to_roll = int(kwargs.get('amount_to_roll', DEFAULT_TIMES_TO_ROLL))
        numbers = np.random.choice(range(dice_min, dice_max + 1), size=times_to_roll, replace=True)
        return ', '.join(f'{n}' for n in numbers)
