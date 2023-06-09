import numpy as np
from game_logic.igame_state import IGameState

from player.mcts.mcts_node import MctsNode


class Ucb1TunedNode(MctsNode):
    @property
    def variance_bound(self):
        return self.reward_squared / self.number_of_runs - self.sample_mean ** 2
    
    
    @property
    def eval(self) -> float:
        ratio_of_visits = np.sqrt(np.log(self.parent.number_of_runs) / self.number_of_runs)
        return self.sample_mean + np.sqrt(ratio_of_visits * min(0.25, self.variance_bound + 2 * ratio_of_visits))
    

    def add_child(self, action: int, game_state: IGameState):
        child = Ucb1TunedNode(game_state, action, self)
        self.untried_actions.remove(action)
        self.children.append(child)

        return child
