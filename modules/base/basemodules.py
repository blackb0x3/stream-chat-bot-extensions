from shared import constants

import numpy as np


class RockPaperScissorsBase(object):
    ROCK = 'rock'
    PAPER = 'paper'
    SCISSORS = 'scissors'
    LIZARD = 'lizard'
    SPOCK = 'spock'

    def __init__(self, **kwargs) -> None:
        self.rules_str: str = kwargs.get('rules', constants.EMPTY_STRING)
        self.options: list = kwargs.get('options', list())
        self.winning_outcomes: dict[tuple, bool] = kwargs.get('winning_outcomes', dict())

    async def rules(self):
        return self.rules_str

    async def play(self, **kwargs):
        player_name = kwargs.get('player_name', 'player')
        player_choice = kwargs.get('choice')

        if player_choice == '' or player_choice is None:
            raise ValueError('player choice not provided!')

        if player_choice not in self.options:
            raise ValueError(f'unknown player choice {player_choice}')            

        computer_choice = str(np.random.choice(self.options))

        if player_choice.lower() == computer_choice.lower():
            return f'It\'s a tie {self._format_result(player_choice, computer_choice)}'
        if (player_choice, computer_choice) in self.winning_outcomes:
            return f'{player_name} wins {self._format_result(player_choice, computer_choice)}'
        else:
            return f'bot wins {self._format_result(player_choice, computer_choice)}'

    def _format_result(self, player_choice: str, computer_choice: str):
        return f'({player_choice} vs {computer_choice})'
