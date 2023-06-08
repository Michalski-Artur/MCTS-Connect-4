from game_visualizer.igame_visualizer import IGameVisualizer
import numpy as np


class ConsoleGameVisualizer(IGameVisualizer):
    def show_current_board(self, board: np.ndarray):
        board_size = board.shape
        for row in range(board_size[0]):
            print("|")
            for column in range(board_size[1]):
                print(board[row][column])
                print("|")
