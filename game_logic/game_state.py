import numpy as np

from game_logic.game_config import GameConfig
from game_logic.igame_state import IGameState
from game_logic.game_status import GameStatus


class GameState(IGameState):

    def __init__(self, game_config: GameConfig):
        self._game_config = game_config
        self._board = np.zeros(shape=(game_config.rows_number, game_config.columns_number))
        self._is_first_player_move = True
        self._game_status = GameStatus.InProgress
        self._available_moves = list(range(game_config.columns_number))

    @property
    def game_status(self) -> GameStatus:
        return self._game_status

    @property
    def available_moves(self) -> list:
        return self._available_moves

    @property
    def game_config(self) -> GameConfig:
        return self._game_config

    @property
    def board(self) -> np.ndarray:
        return self._board

    @property
    def is_first_player_move(self) -> bool:
        return self._is_first_player_move

    def make_move(self, column_index) -> None:
        if column_index not in self.available_moves:
            raise Exception("Specified move is not available")

        row_index = 0
        while self.board[row_index][column_index] != 0:
            row_index += 1

        player_token = 1 if self.is_first_player_move else -1
        self._board[row_index][column_index] = player_token

        if row_index == self._game_config.rows_number - 1:
            self._available_moves.remove(column_index)

        if self.has_winning_sequence(row_index, column_index, player_token):
            self._game_status = GameStatus.FirstPlayerWon if self.is_first_player_move else GameStatus.SecondPlayerWon
        elif not self.available_moves:
            self._game_status = GameStatus.Draw

        self._is_first_player_move = not self.is_first_player_move

    def has_winning_sequence(self, last_move_row, last_move_column, player_token):
        return self.four_in_column(last_move_row, last_move_column, player_token) or \
               self.four_in_row(last_move_row, last_move_column, player_token) or \
               self.four_in_positive_diagonal(last_move_row, last_move_column, player_token) or \
               self.four_in_negative_diagonal(last_move_row, last_move_column, player_token)

    def four_in_row(self, last_move_row, last_move_column, player_token):
        row = last_move_row
        column = last_move_column - 1
        tokens_sum = player_token
        while column >= 0 and self._board[row][column] == player_token:
            column -= 1
            tokens_sum += player_token
        column = last_move_column + 1
        while column < self._game_config.columns_number and self._board[row][column] == player_token:
            column += 1
            tokens_sum += player_token

        return abs(tokens_sum) >= 4

    def four_in_column(self, last_move_row, last_move_column, player_token):
        if last_move_row < 3:
            return False

        row = last_move_row - 1
        column = last_move_column
        tokens_sum = player_token
        while row >= 0 and self._board[row][column] == player_token:
            row -= 1
            tokens_sum += player_token
        return abs(tokens_sum) >= 4

    def four_in_positive_diagonal(self, last_move_row, last_move_column, player_token):
        row = last_move_row + 1
        column = last_move_column + 1
        tokens_sum = player_token
        while column < self._game_config.columns_number and \
                row < self._game_config.rows_number and \
                self._board[row][column] == player_token:
            column += 1
            row += 1
            tokens_sum += player_token

        row = last_move_row - 1
        column = last_move_column - 1
        while column >= 0 and \
                row >= 0 and \
                self._board[row][column] == player_token:
            column -= 1
            row -= 1
            tokens_sum += player_token

        return abs(tokens_sum) >= 4

    def four_in_negative_diagonal(self, last_move_row, last_move_column, player_token):
        row = last_move_row + 1
        column = last_move_column - 1
        tokens_sum = player_token
        while column >= 0 and \
                row < self._game_config.rows_number and \
                self._board[row][column] == player_token:
            column -= 1
            row += 1
            tokens_sum += player_token

        row = last_move_row - 1
        column = last_move_column + 1
        while column < self._game_config.columns_number and \
                row >= 0 and \
                self._board[row][column] == player_token:
            column += 1
            row -= 1
            tokens_sum += player_token

        return abs(tokens_sum) >= 4

    def get_results_for_player(self, is_first_player) -> float:
        match self.game_status:
            case GameStatus.InProgress:
                raise Exception("game_logic isn't over yet")
            case GameStatus.FirstPlayerWon:
                return 1 if is_first_player else 0
            case GameStatus.SecondPlayerWon:
                return 0 if is_first_player else 1
            case GameStatus.Draw:
                return 0.5

    def clone(self):  # -> GameState
        game_state_copy = GameState(self._game_config)
        game_state_copy._board = self.board.copy()
        game_state_copy._available_moves = self.available_moves.copy()
        game_state_copy._game_status = self.game_status
        game_state_copy._is_first_player_move = self.is_first_player_move

        return game_state_copy
