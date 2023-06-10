from player.mcts.mcts_player import MctsPlayer
from player.ucb1_tuned.ucb1_tuned_node import Ucb1TunedNode
from game_logic.igame_state import IGameState


class Ucb1TunedPlayer(MctsPlayer):
    def get_tree_root(self, game_state: IGameState):
        return Ucb1TunedNode(game_state, None, None)
