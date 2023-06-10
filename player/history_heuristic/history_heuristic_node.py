import random

from game_logic.game_status import GameStatus
from game_logic.igame_state import IGameState
from player.mcts.imcts_node import IMctsNode

from player.mcts.mcts_node import MctsNode


class HistoryHeuristicNode(MctsNode):

    def __init__(self, game_state: IGameState, action: int, parent: IMctsNode, epsilon = 0):
        super().__init__(game_state, action, parent)
        self._epsilon = epsilon

    @property
    def epsilon(self) -> float:
        return self._epsilon

    def simulate(self, state):
        actions_history = self.get_actions_history_dictionary()
        while state.game_status == GameStatus.InProgress:
            p = random.random()
            if p < self.epsilon:
                # Get first available move based on actions history
                state.make_move(next((action for action in actions_history if action in state.available_moves),
                                     random.choice(state.available_moves)))
            else:
                state.make_move(random.choice(state.available_moves))
        return state

    def get_actions_history_dictionary(self):
        children = [child for child in self.children if child.number_of_runs > 0]
        return {child.action: child.sample_mean for child in sorted(children, key=lambda child: child.sample_mean)}
