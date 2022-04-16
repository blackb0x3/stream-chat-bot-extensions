import numpy as np

from modules.base.basemodules import RockPaperScissorsBase

RULES = 'Scissors cuts paper. Paper covers rock. Rock crushes Lizard. Lizard poisons Spock. Spock destroys Scissors. Scissors decapitates Lizard. Lizard eats Paper. Paper disproves Spock. Spock vaporizes Rock. Rock crushes Scissors.'
ROCK = RockPaperScissorsBase.ROCK
PAPER = RockPaperScissorsBase.PAPER
SCISSORS = RockPaperScissorsBase.SCISSORS
LIZARD = RockPaperScissorsBase.LIZARD
SPOCK = RockPaperScissorsBase.SPOCK

OPTIONS = [ ROCK, PAPER, SCISSORS, LIZARD, SPOCK ]

WINNING_OUTCOMES = {
    (SCISSORS, PAPER): True,
    (PAPER, ROCK): True,
    (ROCK, LIZARD): True,
    (LIZARD, SPOCK): True,
    (SPOCK, SCISSORS): True,
    (SCISSORS, LIZARD): True,
    (LIZARD, PAPER): True,
    (PAPER, SPOCK): True,
    (SPOCK, ROCK): True,
    (ROCK, SCISSORS): True
}


class RockPaperScissorsLizardSpock(RockPaperScissorsBase):
    def __init__(self) -> None:
        RockPaperScissorsBase.__init__(self, rules=RULES, options=OPTIONS, winning_outcomes=WINNING_OUTCOMES)
