import string
from abc import ABC, abstractmethod

from game_logic.igame_state import IGameState


class IPlayer(ABC):

    @abstractmethod
    def get_and_make_next_move_for_player(self, game_state: IGameState) -> int:
        """Make and return next move for the player"""
        pass

    @property
    @abstractmethod
    def player_name(self) -> string:
        """Property representing player name"""
        pass
