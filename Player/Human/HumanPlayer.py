from Game.IGameState import IGameState
from Player.IPlayer import IPlayer


class HumanPlayer(IPlayer):

    def get_and_make_next_move_for_player(self, game_state: IGameState) -> int:
        # TODO
        # Should wait for user move selection, validate whether move is available and if so make it
        raise NotImplementedError
