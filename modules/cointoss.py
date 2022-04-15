from shared import helpers

HEADS = 'heads'
TAILS = 'tails'


class CoinToss(object):
    def __init__(self) -> None:
        pass

    def heads(self):
        return HEADS

    def tails(self):
        return TAILS

    def flip(self):
        show_heads = helpers.get_random_bool()
        return HEADS if show_heads else TAILS

    def customflip(self, **kwargs):
        heads_choice = kwargs.get('heads', HEADS)
        tails_choice = kwargs.get('tails', TAILS)
        flip = self.flip()
        return heads_choice if flip == HEADS else tails_choice
