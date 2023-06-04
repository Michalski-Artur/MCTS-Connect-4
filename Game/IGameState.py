from abc import ABC, abstractmethod
import numpy as np

from Game.GameConfig import GameConfig
from Game.GameStatus import GameStatus


class IGameState(ABC):
    @property
    @abstractmethod
    def game_config(self) -> GameConfig:
        """Property representing game config"""
        pass

    @property
    @abstractmethod
    def board(self) -> np.ndarray:
        """Property representing current board"""
        pass

    @property
    @abstractmethod
    def game_status(self) -> GameStatus:
        """Property representing current game status"""
        pass

    @property
    @abstractmethod
    def available_moves(self) -> list:
        """Property representing currently available moves"""
        pass

    @property
    @abstractmethod
    def is_first_player_move(self) -> bool:
        """Property representing current moves belong to first player"""
        pass

    @abstractmethod
    def make_move(self, column_index: int) -> None:
        """Insert by the current player"""
        pass

    @abstractmethod
    def get_results_for_player(self, is_first_player) -> float:
        """Return result of the game as a number. By default 1 for win, 0 for lose and 0.5 for draw"""
        pass

    @abstractmethod
    def clone(self):
        """Return copy of game state"""
        pass

