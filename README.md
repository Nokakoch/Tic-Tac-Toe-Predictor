# Tic Tac Toe predictor
In this project, we are gonna to make a tic tac toe predictor which helps you to win your games based on 255168 possible moves.

# Analyze dataset

This dataset contains 255168 records and 10 columns:
- Winner: X, O, -(draw)
- Move 1-X (Row-Col): (0-0, ..., 2-2)
- Move 2-O (Row-Col): (0-0, ..., 2-2)
- Move 3-X (Row-Col): (0-0, ..., 2-2)
- Move 4-O (Row-Col): (0-0, ..., 2-2)
- Move 5-X (Row-Col): (0-0, ..., 2-2)
- Move 6-O (Row-Col): (0-0, ..., 2-2)
- Move 7-X (Row-Col): (0-0, ..., 2-2)
- Move 8-O (Row-Col): (0-0, ..., 2-2)
- Move 9-X (Row-Col): (0-0, ..., 2-2)

And there is some facts that comes from our datas:
- In 51.4% of games, winner is X or who play first. So if you start game, you have much better chance to win (+20.9%).
- 21.4% of matches never reach eighth move.
- 49.9% of matches never reach ninth move.
- At least 5 moves need to end a game.