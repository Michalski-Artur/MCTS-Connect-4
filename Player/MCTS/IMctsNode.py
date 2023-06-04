from abc import ABC, abstractmethod

from Game.IGameState import IGameState


class IMctsNode(ABC):
    @property
    @abstractmethod
    def action(self) -> int:
        """Property representing column to put token into"""
        pass

    @property
    @abstractmethod
    def game_state(self) -> IGameState:
        """Property representing current state of the game"""
        pass

    @property
    @abstractmethod
    def parent(self):  # -> IMctsNode
        """Property representing parent of the node"""
        pass

    @property
    @abstractmethod
    def number_of_runs(self) -> int:
        """Property representing number of times node has been evaluated"""
        pass

    @property
    @abstractmethod
    def number_of_wins(self) -> float:
        """Property representing aggregated score for the node"""
        pass

    @property
    @abstractmethod
    def exploration_value(self) -> float:
        """Property representing exploration value for the node"""
        pass

    @property
    @abstractmethod
    def exploitation_value(self) -> float:
        """Property representing exploitation value for the node"""
        pass

    @property
    @abstractmethod
    def uct(self) -> float:
        """Property representing uct value for the node"""
        pass
