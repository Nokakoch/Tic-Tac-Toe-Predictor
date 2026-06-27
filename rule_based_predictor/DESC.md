# Rule Based Predictor

There are two main goals in Tic-Tac-Toe: try to win the game, otherwise don't let your opponent win.

The problem with the simple baseline predictor was that it only looked at the win rate of the next move. That works only if the opponent also plays random moves and doesn't try to win.

However, our dataset contains every possible move, not only good moves. So the predictor eventually suggests moves based on all possible moves not the best ones.

In this step, we solve this problem by adding simple game rules, such as detecting immediate winning moves or blocking the opponent's winning move.
