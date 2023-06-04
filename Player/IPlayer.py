from abc import ABC, abstractmethod

from Game.IGameState import IGameState


class IPlayer(ABC):

    @abstractmethod
    def get_and_make_next_move_for_player(self, game_state: IGameState) -> int:
        """Make and return next move for the player"""
        pass
