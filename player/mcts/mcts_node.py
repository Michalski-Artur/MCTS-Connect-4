import random
import time
import numpy as np

from game_logic.game_status import GameStatus
from game_logic.igame_state import IGameState
from player.mcts.imcts_node import IMctsNode


class MctsNode(IMctsNode):
    def __init__(self, game_state: IGameState, action: int, parent: IMctsNode):
        self._game_state = game_state
        self._action = action
        self._parent = parent
        self._reward = 0
        self._reward_squared = 0
        self._number_of_runs = 0
        self.untried_actions = list(game_state.available_moves)
        self.children = list()

    @property
    def game_state(self) -> IGameState:
        return self._game_state

    @property
    def action(self) -> int:
        return self._action

    @property
    def parent(self) -> IMctsNode:
        return self._parent

    @property
    def number_of_runs(self) -> int:
        return self._number_of_runs

    @property
    def reward(self) -> float:
        return self._reward

    @property
    def reward_squared(self) -> float:
        return self._reward_squared

    @property
    def sample_mean(self) -> float:
        return self.reward / self.number_of_runs

    @property
    def eval(self) -> float:
        return self.sample_mean + np.sqrt(np.log(self.parent.number_of_runs) / self.number_of_runs)

    def build_tree(self, should_continue):
        iteration = 1
        start_time = time.time()

        while should_continue(iteration, time.time() - start_time):
            node = self
            state = self.game_state.clone()

            # Select
            node = self.select(node, state)

            # Expand
            node = self.expand(node, state)

            # Simulate
            self.simulate(node, state)

            # Backpropagate
            self.backpropagate(node, state)

            iteration += 1

    @staticmethod
    def select(node, state):
        while not node.untried_actions and node.game_state.available_moves:
            node = node.select_child()
            state.make_move(node.action)
        return node

    @staticmethod
    def expand(node, state):
        if node.untried_actions:
            action = random.choice(node.untried_actions)
            state.make_move(action)
            node = node.add_child(action, state)
        return node

    @staticmethod
    def simulate(node, state):
        while state.game_status == GameStatus.InProgress:
            state.make_move(random.choice(state.available_moves))

    def backpropagate(self, node, state):
        current_reward = state.get_results_for_player(self.game_state.is_first_player_move)
        while node:
            node._number_of_runs += 1
            node._reward += current_reward
            node._reward_squared += current_reward ** 2
            node = node.parent

    def select_child(self):
        return max(self.children, key=lambda child: child.eval)

    def add_child(self, action: int, game_state: IGameState):
        child = MctsNode(game_state, action, self)
        self.untried_actions.remove(action)
        self.children.append(child)

        return child
