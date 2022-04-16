from shared import helpers

HEADS = 'heads'
TAILS = 'tails'


class CoinToss(object):
    def __init__(self) -> None:
        pass

    async def heads(self):
        return HEADS

    async def tails(self):
        return TAILS

    async def flip(self):
        show_heads = helpers.get_random_bool()
        return HEADS if show_heads else TAILS

    async def customflip(self, **kwargs):
        heads_choice = kwargs.get('heads', HEADS)
        tails_choice = kwargs.get('tails', TAILS)
        flip = self.flip()
        return heads_choice if flip == HEADS else tails_choice
