from enum import Enum


class GameStatus(Enum):
    InProgress = 1
    FirstPlayerWon = 2
    SecondPlayerWon = 3
    Draw = 4
