from Game.Game import Game
from Game.GameConfig import GameConfig
from Game.GameState import GameState
from GameVisualizer.ConsoleGameVisualizer import ConsoleGameVisualizer
from Player.Human.HumanPlayer import HumanPlayer
from Player.MCTS.MctsConfiguration import MctsConfiguration
from Player.MCTS.MctsPlayer import MctsPlayer


def main():
    first_player = HumanPlayer()

    # TODO
    # Provide values for mcts configuration
    mcts_configuration = MctsConfiguration()
    second_player = MctsPlayer(mcts_configuration)

    game_config = GameConfig()
    game_state = GameState(game_config)
    game_visualizer = ConsoleGameVisualizer()
    game = Game(game_state, first_player, second_player, game_visualizer)

    game.play()


if __name__ == "__main__":
    main()
