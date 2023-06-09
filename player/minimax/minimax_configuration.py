class MinimaxConfiguration:
    def __init__(self, max_depth: int):
        self._max_depth = max_depth

    @property
    def max_depth(self) -> int:
        return self._max_depth
