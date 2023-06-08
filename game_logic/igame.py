from abc import ABC, abstractmethod

from game_logic.igame_state import IGameState
from game_visualizer.igame_visualizer import IGameVisualizer
from player.iplayer import IPlayer


class IGame(ABC):
    @property
    @abstractmethod
    def game_state(self) -> IGameState:
        """Property representing current state of the game"""
        pass

    @property
    @abstractmethod
    def first_player(self) -> IPlayer:
        """Property representing first player"""
        pass

    @property
    @abstractmethod
    def second_player(self) -> IPlayer:
        """Property representing second player"""
        pass

    @property
    @abstractmethod
    def game_visualizer(self) -> IGameVisualizer:
        """Property representing game visualizer"""
        pass

    @abstractmethod
    def play(self) -> None:
        """Run game for setted up agents"""
        pass
