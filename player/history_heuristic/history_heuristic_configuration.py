from player.mcts.mcts_configuration import MctsConfiguration


class HistoryHeuristicConfiguration(MctsConfiguration):
    def __init__(self, max_iterations: int, time_limit, epsilon: float):
        super().__init__(max_iterations, time_limit)
        self._epsilon = epsilon

    @property
    def epsilon(self):
        return self._epsilon
