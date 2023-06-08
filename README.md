# MCTS-Connect-4

## Project structure
### game_logic:
- all features required for game logic
- igame - responsible for aggregating game state, players, game visualizer and running game. Implementation: game
- igame_state - responsible for aggregating data about current state of the game: state of the board, state of the game, game config, available moves, whose move is right now. Implementation: game_state
- game_config - aggregates data about the game configuration. For now only data about size of the board
- game_status - enum representing current state of the game. Game is either: in progress, first player won, second player won or draw
 
### game_visualizer:
- interface and its implementations for visualizing current state of the game
- console_game_visualizer - basic game visualization on the console

### player:
- interface and its implementations for algorithm representing game player
- human_player - for now asks through console for the next move
- mcts_player - basic mcts player. When asked for the move it builds tree using mcts algorithm and returns node with action (move) that has highest number of runs. Tree is build as long as max number of iterations and time are not exceeded (these values are stored in mcts_configuration)