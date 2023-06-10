import numpy as np

from game_logic.game_status import GameStatus
from game_logic.igame_state import IGameState
from player.mcts.mcts_node import MctsNode
from player.mcts.imcts_node import IMctsNode


class ScoreBoundedMctsNode(MctsNode):
    def __init__(self, game_state: IGameState, action: int, parent: IMctsNode):
        super().__init__(game_state, action, parent)
        self._score_lower_bound = -np.inf
        self._score_upper_bound = np.inf

    def select(self, node, state):
        while not node.untried_actions and node.game_state.available_moves:
            node = node.select_child(node.game_state.is_first_player_move)
            state.make_move(node.action)
        return node, state
    
    def backpropagate(self, node, state):
        current_reward = state.get_results_for_player(self.game_state.is_first_player_move)

        node._number_of_runs += 1
        node._reward += current_reward
        node._reward_squared += current_reward ** 2
        node.update_score_bounds(current_reward, node.game_state.is_first_player_move, True)
        node = node.parent
        
        while node:
            node._number_of_runs += 1
            node._reward += current_reward
            node._reward_squared += current_reward ** 2
            node.update_score_bounds(node.reward, node.game_state.is_first_player_move, False)
            node = node.parent

    def select_child(self, is_max: bool):
        if is_max:
            bounded_children = [child for child in self.children if child._score_upper_bound >= self._score_lower_bound]
        else:
            bounded_children = [child for child in self.children if child._score_lower_bound <= self._score_upper_bound]

        return max(bounded_children, key=lambda child: child.eval)

    def update_score_bounds(self, score: float, is_max: bool, is_terminal: bool):
        if is_terminal:
            self._score_upper_bound = score
            self._score_lower_bound = score
        elif is_max:
            self._score_lower_bound = max(child._score_lower_bound for child in self.children)
            self._score_upper_bound = max(child._score_upper_bound for child in self.children)
        else:
            self._score_lower_bound = min(child._score_lower_bound for child in self.children)
            self._score_upper_bound = min(child._score_upper_bound for child in self.children)
        
