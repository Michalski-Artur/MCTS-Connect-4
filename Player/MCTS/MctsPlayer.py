from Game.IGameState import IGameState
from Player.IPlayer import IPlayer
from Player.MCTS.MctsConfiguration import MctsConfiguration
from Player.MCTS.MctsNode import MctsNode


class MctsPlayer(IPlayer):
    def __init__(self, mcts_configuration: MctsConfiguration):
        self.mcts_configuration = mcts_configuration

    def get_and_make_next_move_for_player(self, game_state: IGameState) -> int:
        top_action = self.get_top_action(game_state)
        game_state.make_move(top_action)
        return top_action

    def get_top_action(self, game_state: IGameState):
        root = MctsNode(game_state, None, None)

        # TODO
        # Provide stop condition
        root.build_tree()

        return max(root.children, key=lambda child: child.number_of_runs).action
