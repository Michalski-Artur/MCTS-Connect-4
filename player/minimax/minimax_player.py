import math

import numpy as np

from game_logic.game_status import GameStatus
from game_logic.igame_state import IGameState
from player.iplayer import IPlayer
from player.minimax.minimax_configuration import MinimaxConfiguration


class MinimaxPlayer(IPlayer):

    def __init__(self, minimax_configuration: MinimaxConfiguration, player_name="Minimax"):
        self.minimax_configuration = minimax_configuration
        self._player_name = player_name
        self._heuristic_fields_values = np.array([
                [3, 4,  5,  7,  5, 4, 3],
                [4, 6,  8, 10,  8, 6, 4],
                [5, 8, 11, 13, 11, 8, 5],
                [5, 8, 11, 13, 11, 8, 5],
                [4, 6,  8, 10,  8, 6, 4],
                [3, 4,  5,  7,  5, 4, 3]
            ])

    @property
    def player_name(self):
        return self._player_name

    # TODO:
    #  If its hardcoded, it cannot be used for other board sizes, maybe it should be generated?
    @property
    def heuristic_fields_values(self):
        return self._heuristic_fields_values

    def get_and_make_next_move_for_player(self, game_state: IGameState) -> int:
        evaluation, move = self.minimax(
            game_state=game_state,
            current_depth=0,
            max_turn=True,
            move=None,
            is_first_player=game_state.is_first_player_move)

        game_state.make_move(move)
        return move

    def minimax(self, game_state, current_depth, max_turn, move, is_first_player) -> (int, int):
        if move is not None:
            game_state = game_state.clone()
            game_state.make_move(move)
        if current_depth == self.minimax_configuration.max_depth or game_state.game_status != GameStatus.InProgress:
            return self.evaluate_state(game_state, is_first_player), move

        if max_turn:
            max_evaluation = -math.inf, None
            for move in game_state.available_moves:
                evaluation = self.minimax(game_state, current_depth + 1, False, move, is_first_player)
                if evaluation[0] > max_evaluation[0]:
                    max_evaluation = evaluation[0], move
            return max_evaluation
        else:
            min_evaluation = math.inf, None
            for move in game_state.available_moves:
                evaluation = self.minimax(game_state, current_depth + 1, True, move, is_first_player)
                if evaluation[0] < min_evaluation[0]:
                    min_evaluation = evaluation[0], move
            return min_evaluation

    def evaluate_state(self, game_state, is_first_player) -> int:
        multiplier = 1 if is_first_player else -1
        match game_state.game_status:
            case GameStatus.InProgress:
                return multiplier * np.sum(game_state.board * self._heuristic_fields_values)
            case GameStatus.FirstPlayerWon:
                return 10000 if is_first_player else -10000
            case GameStatus.SecondPlayerWon:
                return -10000 if is_first_player else 10000
            case GameStatus.Draw:
                return 0
