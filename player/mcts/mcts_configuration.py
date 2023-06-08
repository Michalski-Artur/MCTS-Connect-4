class MctsConfiguration:
    def __init__(self, max_iterations: int, time_limit):
        self._max_iterations = max_iterations
        self._time_limit = time_limit

    @property
    def max_iterations(self) -> int:
        return self._max_iterations

    @property
    def time_limit(self):
        return self._time_limit

