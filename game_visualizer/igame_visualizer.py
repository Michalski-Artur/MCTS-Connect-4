from abc import ABC, abstractmethod


class IGameVisualizer(ABC):

    @abstractmethod
    def show_current_board(self, board):
        pass
