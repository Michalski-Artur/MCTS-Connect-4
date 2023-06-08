from game_logic.game_status import GameStatus
from game_logic.igame import IGame
from game_logic.igame_state import IGameState
from game_visualizer.igame_visualizer import IGameVisualizer
from player.iplayer import IPlayer


class Game(IGame):

    def __init__(self,
                 game_state: IGameState,
                 first_player: IPlayer,
                 second_player: IPlayer,
                 game_visualizer: IGameVisualizer):
        self._game_state = game_state
        self._first_player = first_player
        self._second_player = second_player
        self._game_visualizer = game_visualizer

    @property
    def game_state(self) -> IGameState:
        return self._game_state

    @property
    def first_player(self) -> IPlayer:
        return self._first_player

    @property
    def second_player(self) -> IPlayer:
        return self._second_player

    @property
    def game_visualizer(self) -> IGameVisualizer:
        return self.game_visualizer

    def play(self) -> None:
        while self.game_state.game_status is GameStatus.InProgress:
            current_player = self.first_player if self.game_state.is_first_player_move else self.second_player
            current_player.get_and_make_next_move_for_player(self.game_state)
            self.game_visualizer.show_current_board(self.game_state.board)
        print(self.game_state.game_status)
