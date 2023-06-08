from game_visualizer.igame_visualizer import IGameVisualizer
import numpy as np


class ConsoleGameVisualizer(IGameVisualizer):
    def show_current_board(self, board: np.ndarray):
        board_size = board.shape

        print("|", end=" ")
        for column in range(board_size[1]):
            print(column + 1, end=" ")
            print("|", end=" ")
        print()

        for row in reversed(range(board_size[0])):
            print("|", end=" ")
            for column in range(board_size[1]):
                token = " " if board[row][column] == 0 else "X" if board[row][column] == 1 else "O"
                print(token, end=" ")
                print("|", end=" ")
            print()
