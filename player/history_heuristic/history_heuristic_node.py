import random
import time

from game_logic.game_status import GameStatus
from game_logic.igame_state import IGameState
from player.history_heuristic.history_heuristic_player import HistoryHeuristicPlayer

from player.mcts.mcts_node import MctsNode


class HistoryHeuristicNode(MctsNode):

    def build_history_tree(self, should_continue, total_rewards_for_actions, times_actions_has_been_selected, epsilon):
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
            action, current_reward = self.backpropagate(node, state)

            if action not in times_actions_has_been_selected:
                times_actions_has_been_selected[action] = 0
            times_actions_has_been_selected[action] += 1

            if action not in total_rewards_for_actions:
                total_rewards_for_actions[action] = 0
            total_rewards_for_actions[action] += current_reward

            iteration += 1

    def add_child(self, action: int, game_state: IGameState):
        child = HistoryHeuristicNode(game_state, action, self)
        self.untried_actions.remove(action)
        self.children.append(child)

        return child

    @staticmethod
    def simulate(node, state):
        while state.game_status == GameStatus.InProgress:
            p = random.random()
            if p < HistoryHeuristicPlayer.configuration.epsilon:
                state.make_move(random.choice(state.available_moves))
            else

    def backpropagate(self, node, state):
        current_reward = state.get_results_for_player(self.game_state.is_first_player_move)
        action = node.action
        while node:
            node._number_of_runs += 1
            node._reward += current_reward
            node._reward_squared += current_reward ** 2
            action = node.action
            node = node.parent
        return action, current_reward

    def get




