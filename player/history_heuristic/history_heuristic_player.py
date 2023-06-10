from game_logic.igame_state import IGameState
from player.history_heuristic.history_heuristic_configuration import HistoryHeuristicConfiguration
from player.history_heuristic.history_heuristic_node import HistoryHeuristicNode
from player.mcts.mcts_player import MctsPlayer
from player.mcts.imcts_node import IMctsNode


class HistoryHeuristicPlayer(MctsPlayer):
    node_type: IMctsNode = HistoryHeuristicNode

    def __init__(self, history_heuristic_configuration: HistoryHeuristicConfiguration):
        super().__init__(history_heuristic_configuration)
        self._configuration = history_heuristic_configuration
        self._total_rewards_for_actions = dict()
        self._times_actions_has_been_selected = dict()

    @property
    def configuration(self):
        return self._configuration

    @property
    def total_rewards_for_actions(self) -> dict:
        return self._total_rewards_for_actions

    @property
    def times_actions_has_been_selected(self) -> dict:
        return self._times_actions_has_been_selected

    def get_top_action(self, game_state: IGameState):
        root = self.node_type(game_state, None, None)

        def should_continue_building_tree(iteration, time):
            return iteration < self.configuration.max_iterations and \
                   time < self.configuration.time_limit

        root.build_tree(should_continue_building_tree,
                        self.total_rewards_for_actions,
                        self.times_actions_has_been_selected,
                        self.configuration.epsilon)

        return max(root.children, key=lambda child: child.number_of_runs).action
