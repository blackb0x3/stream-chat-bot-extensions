from modules.base.basemodules import RockPaperScissorsBase


RULES = 'Scissors cuts paper. Paper covers rock. Rock crushes Scissors.'
ROCK = RockPaperScissorsBase.ROCK
PAPER = RockPaperScissorsBase.PAPER
SCISSORS = RockPaperScissorsBase.SCISSORS

OPTIONS = [ ROCK, PAPER, SCISSORS ]

WINNING_OUTCOMES = {
    (SCISSORS, PAPER): True,
    (PAPER, ROCK): True,
    (ROCK, SCISSORS): True
}


class RockPaperScissors(RockPaperScissorsBase):
    def __init__(self) -> None:
        RockPaperScissorsBase.__init__(self, rules=RULES, options=OPTIONS, winning_outcomes=WINNING_OUTCOMES)
