from game_logic.game import Game
from game_logic.game_config import GameConfig
from game_logic.game_state import GameState
from game_visualizer.console_game_visualizer import ConsoleGameVisualizer
from player.history_heuristic.history_heuristic_configuration import HistoryHeuristicConfiguration
from player.history_heuristic.history_heuristic_player import HistoryHeuristicPlayer
from player.human.human_player import HumanPlayer
from player.mcts.mcts_configuration import MctsConfiguration
from player.mcts.mcts_player import MctsPlayer
from player.minimax.minimax_configuration import MinimaxConfiguration
from player.minimax.minimax_player import MinimaxPlayer
from player.score_bounded_mcts.score_bounded_mcts_player import ScoreBoundedMctsPlayer
from player.ucb1_tuned.ucb1_tuned_player import Ucb1TunedPlayer


def main():
    # Human
    # first_player = HumanPlayer()
    # second_player = HumanPlayer()

    # MCTS
    mcts_configuration = MctsConfiguration(30_000, 10)
    first_player = MctsPlayer(mcts_configuration)
    # second_player = MctsPlayer(mcts_configuration)

    # UCB1
    ucb_configuration = MctsConfiguration(30_000, 10)
    # first_player = Ucb1TunedPlayer(ucb_configuration)
    # second_player = Ucb1TunedPlayer(ucb_configuration)

    # History
    history_heuristic_configuration = HistoryHeuristicConfiguration(30_000, 10, 0.3)
    # first_player = HistoryHeuristicPlayer(history_heuristic_configuration)
    # second_player = HistoryHeuristicPlayer(history_heuristic_configuration)

    # Minimax
    minimax_configuration = MinimaxConfiguration(4)  # 7 takes a while
    # first_player = MinimaxPlayer(minimax_configuration)
    second_player = MinimaxPlayer(minimax_configuration)

    # ScoreBoundedMcts
    score_bounded_mcts_configuration = MctsConfiguration(30_000, 10)
    # first_player = ScoreBoundedMctsPlayer(mcts_configuration)
    # second_player = ScoreBoundedMctsPlayer(mcts_configuration)

    game_config = GameConfig()
    game_state = GameState(game_config)
    game_visualizer = ConsoleGameVisualizer()
    game = Game(game_state, first_player, second_player, game_visualizer)

    game.play()


if __name__ == "__main__":
    main()
