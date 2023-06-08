from game_logic.igame_state import IGameState
from player.iplayer import IPlayer


class HumanPlayer(IPlayer):

    def get_and_make_next_move_for_player(self, game_state: IGameState) -> int:
        # TODO:
        # Alter this part when adding integration with GUI

        while True:
            try:
                move = int(input('Please select column to insert token into.\n'))
                if move in game_state.available_moves:
                    return move
                print('Invalid move selected.')
            except ValueError:
                print('Invalid move selected. Only integer values are supported')
