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

    def add_child(self, action: int, game_state: IGameState):
        child = HistoryHeuristicNode(game_state, action, self)
        self.untried_actions.remove(action)
        self.children.append(child)

        return child

    def simulate(self, state):
        actions_history = self.get_actions_history_dictionary()
        while state.game_status == GameStatus.InProgress:
            p = random.random()
            if p < self.epsilon:
                # Get first available move based on actions history
                for action in actions_history:
                    if action in state.available_moves:
                        state.make_move(action)
                        break
            else:
                state.make_move(random.choice(state.available_moves))
        return state

    def get_actions_history_dictionary(self):
        children = filter(lambda child: child.number_of_runs > 0, self.children)
        return {child.action: child.sample_mean for child in sorted(children, key=lambda child: child.sample_mean)}