from game_logic.igame_state import IGameState
from player.history_heuristic.history_heuristic_configuration import HistoryHeuristicConfiguration
from player.history_heuristic.history_heuristic_node import HistoryHeuristicNode
from player.mcts.mcts_player import MctsPlayer


class HistoryHeuristicPlayer(MctsPlayer):
    def __init__(self, history_heuristic_configuration: HistoryHeuristicConfiguration, player_name="HistoryHeuristic"):
        super().__init__(history_heuristic_configuration)
        self._configuration = history_heuristic_configuration
        self._total_rewards_for_actions = dict()
        self._times_actions_has_been_selected = dict()
        self._player_name = player_name

    @property
    def player_name(self):
        return self._player_name

    @property
    def configuration(self):
        return self._configuration

    def get_tree_root(self, game_state: IGameState):
        return HistoryHeuristicNode(game_state, None, None, self.configuration.epsilon)
