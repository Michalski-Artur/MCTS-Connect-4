from game_logic.game import Game
from game_logic.game_config import GameConfig
from game_logic.game_state import GameState
from game_visualizer.console_game_visualizer import ConsoleGameVisualizer
from player.human.human_player import HumanPlayer
from player.mcts.mcts_configuration import MctsConfiguration
from player.mcts.mcts_player import MctsPlayer


def main():
    first_player = HumanPlayer()

    mcts_configuration = MctsConfiguration(30_000, 10)
    second_player = MctsPlayer(mcts_configuration)

    game_config = GameConfig()
    game_state = GameState(game_config)
    game_visualizer = ConsoleGameVisualizer()
    game = Game(game_state, first_player, second_player, game_visualizer)

    game.play()


if __name__ == "__main__":
    main()
