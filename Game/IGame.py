from abc import ABC, abstractmethod

from Game.IGameState import IGameState
from GameVisualizer.IGameVisualizer import IGameVisualizer
from Player.IPlayer import IPlayer


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
