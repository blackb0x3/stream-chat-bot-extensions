import numpy as np

RULES = 'Scissors cuts paper. Paper covers rock. Rock crushes Scissors.'
ROCK = 'rock'
PAPER = 'paper'
SCISSORS = 'scissors'

OPTIONS = [ ROCK, PAPER, SCISSORS ]

WINNING_OUTCOMES = {
    (SCISSORS, PAPER): True,
    (PAPER, ROCK): True,
    (ROCK, SCISSORS): True
}


class RockPaperScissors(object):
    def __init__(self) -> None:
        pass

    def rules(self):
        return RULES

    def play(self, **kwargs):
        player_name = kwargs.get('player_name', 'player')
        player_choice = kwargs.get('choice')

        if player_choice == '' or player_choice is None:
            raise ValueError('player choice not provided!')

        if player_choice not in OPTIONS:
            raise ValueError(f'unknown player choice {player_choice}')            

        computer_choice = str(np.random.choice(OPTIONS))

        if player_choice.lower() == computer_choice.lower():
            return f'It\'s a tie {self.__format_result(player_choice, computer_choice)}'
        if (player_choice, computer_choice) in WINNING_OUTCOMES:
            return f'{player_name} wins {self.__format_result(player_choice, computer_choice)}'
        else:
            return f'bot wins {self.__format_result(player_choice, computer_choice)}'

    def __format_result(self, player_choice: str, computer_choice: str):
        return f'({player_choice} vs {computer_choice})'
