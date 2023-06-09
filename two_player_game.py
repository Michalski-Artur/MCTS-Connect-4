import itertools
from game_logic.game import Game
from game_logic.game_config import GameConfig
from game_logic.game_state import GameState
from game_logic.game_status import GameStatus
from player.mcts.mcts_configuration import MctsConfiguration
from player.mcts.mcts_player import MctsPlayer
import threading
import time


def play_iterative(times=100, game_config=GameConfig()):
    mcts_configuration = MctsConfiguration(30_000, 10)
    first_player, second_player = MctsPlayer(mcts_configuration), MctsPlayer(mcts_configuration)
    score = {'first_player': {'player_type': first_player.get_name(), 'score': 0}, 'second_player': {'player_type': second_player.get_name(), 'score': 0}}

    start_time = time.time()
    for _ in range(times):
        game_state = GameState(game_config)
        game = Game(game_state, first_player, second_player, print_game_stats=False)
        if game.play() == GameStatus.FirstPlayerWon:
            score['first_player']['score'] += 1
        else:
            score['second_player']['score'] += 1
    end_time = time.time()
    runtime = end_time - start_time
    print(f"Runtime for {times} games is: {round(runtime/60, 4)} min")

    return score


def play_single_game(game_config, first_player, second_player, score_mutex=None, shared_score=None):
    game_state = GameState(game_config)
    game = Game(game_state, first_player, second_player, print_game_stats=False)

    winner = game.play()

    score_mutex.acquire()
    if winner == GameStatus.FirstPlayerWon:
        shared_score['first_player']['score'] += 1
    else:
        shared_score['second_player']['score'] += 1
    score_mutex.release()


def play_in_threads(game_config, first_player, second_player, times=10):
    score = {'first_player': {'player_type': first_player.get_name(), 'score': 0}, 'second_player': {'player_type': second_player.get_name(), 'score': 0}}
    score_mutex = threading.Lock()
    threads = []

    start_time = time.time()
    for _ in range(times):
        thread = threading.Thread(target=play_single_game, args=(game_config, first_player, second_player, score_mutex, score))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    end_time = time.time()
    runtime = end_time - start_time
    print(f"Runtime for {times} games is: {round(runtime/60, 4)} min")

    return score


def run_experiments(game_config, iterations=50):
    global_scores = dict()

    mcts_configuration = MctsConfiguration(30_000, 10)
    # TODO: after other types of players will be added add them to the list
    players = [MctsPlayer(mcts_configuration), MctsPlayer(mcts_configuration)]

    for player1, player2 in itertools.permutations(players, 2):
        global_scores.update(play_in_threads(game_config, player1, player2, iterations))

    print('GLOBAL SCORES:')
    print(global_scores)

    
def main():
    game_config=GameConfig()
    run_experiments(game_config, iterations=2)

if __name__ == "__main__":
    main()
