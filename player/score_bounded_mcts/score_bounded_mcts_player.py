from game_logic.igame_state import IGameState
from player.mcts.mcts_configuration import MctsConfiguration
from player.mcts.mcts_player import MctsPlayer
from player.score_bounded_mcts.score_bounded_mcts_node import ScoreBoundedMctsNode


class ScoreBoundedMctsPlayer(MctsPlayer):

    def __init__(self, mcts_configuration: MctsConfiguration, player_name="ScoreBoundedMctsPlayer"):
        super().__init__(mcts_configuration, player_name)

    def get_tree_root(self, game_state: IGameState):
        return ScoreBoundedMctsNode(game_state, None, None)