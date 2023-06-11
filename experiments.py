import itertools
import threading
import time

from game_logic.game import Game
from game_logic.game_config import GameConfig
from game_logic.game_state import GameState
from game_logic.game_status import GameStatus
from player.history_heuristic.history_heuristic_configuration import HistoryHeuristicConfiguration

from player.mcts.mcts_configuration import MctsConfiguration
from player.mcts.mcts_player import MctsPlayer
from player.ucb1_tuned.ucb1_tuned_player import Ucb1TunedPlayer
from player.minimax.minimax_configuration import MinimaxConfiguration
from player.minimax.minimax_player import MinimaxPlayer
from player.score_bounded_mcts.score_bounded_mcts_player import ScoreBoundedMctsPlayer
from player.history_heuristic.history_heuristic_player import HistoryHeuristicPlayer


class Experiments:
    def __init__(self, iterations=50):
        self.iterations = iterations
        self.game_config = GameConfig()
        self.global_score = list()

    def play_single_game(self, first_player, second_player, score_mutex, score):
        game_state = GameState(self.game_config)
        game = Game(game_state, first_player, second_player, print_game_stats=False)
        game_status = game.play()
        score_mutex.acquire()
        if game_status == GameStatus.Draw:
            score['first_player']['draws'] += 1
            score['first_player']['score'] += 0.5
            score['second_player']['draws'] += 1
            score['second_player']['score'] += 0.5
        elif game_status == GameStatus.FirstPlayerWon:
            score['first_player']['wins'] += 1
            score['first_player']['score'] += 1
            score['second_player']['loses'] += 1
        else:
            score['first_player']['loses'] += 1
            score['second_player']['score'] += 1
            score['second_player']['wins'] += 1
        score_mutex.release()

    def play_in_threads(self, first_player, second_player):
        score = {'first_player': {'player_type': first_player.player_name, 'score': 0, 'wins': 0, 'loses': 0, 'draws': 0},
                 'second_player': {'player_type': second_player.player_name, 'score': 0, 'wins': 0, 'loses': 0, 'draws': 0}}

        score_mutex = threading.Lock()
        threads = []

        start_time = time.time()
        for _ in range(self.iterations):
            thread = threading.Thread(target=self.play_single_game,
                                      args=(first_player, second_player, score_mutex, score))
            thread.start()
            threads.append(thread)
        for thread in threads:
            thread.join()
        end_time = time.time()
        runtime = end_time - start_time
        print(f"Runtime for {self.iterations} iterations is: {round(runtime / 60, 4)} min")
        return score

    def run_experiments(self):
        mcts_config = MctsConfiguration(30_000, 10)
        history_heuristic_config = HistoryHeuristicConfiguration(30_000, 10, 0.3)
        minimax_config = MinimaxConfiguration(4)
        self.players = [
            MctsPlayer(mcts_config),
            Ucb1TunedPlayer(mcts_config),
            MinimaxPlayer(minimax_config),
            ScoreBoundedMctsPlayer(mcts_config),
            HistoryHeuristicPlayer(history_heuristic_config)
            ]

        for player1, player2 in itertools.permutations(self.players, 2):
            self.global_score.append(self.play_in_threads(player1, player2))
            print(self.global_score[-1])

        # playing against itself
        for player in self.players:
            self.global_score.append(self.play_in_threads(player, player))

    def print_scores(self):
        print('Results:')
        for game in self.global_score:
            player1 = game['first_player']
            player2 = game['second_player']
            print()
            print(f"Scores: {player1['player_type']}  {player1['score']}:{player2['score']}  {player2['player_type']}")
            print(f"Wins: {player1['player_type']}  {player1['wins']}:{player2['wins']}  {player2['player_type']}")
            print(f"Draws: {player1['player_type']}  {player1['draws']}:{player2['draws']}  {player2['player_type']}")
            print(f"Loses: {player1['player_type']}  {player1['loses']}:{player2['loses']}  {player2['player_type']}")
            print()


def main():
    experiments = Experiments(50)
    experiments.run_experiments()
    experiments.print_scores()

if __name__ == "__main__":
    main()
