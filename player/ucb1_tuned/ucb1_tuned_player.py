from player.mcts.mcts_player import MctsPlayer
from player.ucb1_tuned.ucb1_tuned_node import Ucb1TunedNode
from player.mcts.imcts_node import IMctsNode


class Ucb1TunedPlayer(MctsPlayer):
    node_type: IMctsNode = Ucb1TunedNode