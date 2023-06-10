from game_logic.igame_state import IGameState
from player.iplayer import IPlayer
from player.mcts.imcts_node import IMctsNode
from player.mcts.mcts_configuration import MctsConfiguration
from player.mcts.mcts_node import MctsNode
from player.mcts.imcts_node import IMctsNode


class MctsPlayer(IPlayer):
    node_type: IMctsNode = MctsNode

    def __init__(self, mcts_configuration: MctsConfiguration, player_name="MCTS player"):
        self._configuration = mcts_configuration
        self._player_name = player_name

    @property
    def player_name(self):
        return self._player_name

    @property
    def configuration(self):
        return self._configuration
    
    def get_and_make_next_move_for_player(self, game_state: IGameState) -> int:
        top_action = self.get_top_action(game_state)
        game_state.make_move(top_action)
        return top_action

    def get_top_action(self, game_state: IGameState):
        root = self.node_type(game_state, None, None)

        def should_continue_building_tree(iteration, time):
            return iteration < self.configuration.max_iterations and \
                   time < self.configuration.time_limit

        root.build_tree(should_continue_building_tree)

        return max(root.children, key=lambda child: child.number_of_runs).action
