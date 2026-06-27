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

## Simple baseline predictor

Now let's build our first predictor.

There is only one rule:

**Trust the dataset.**

- No game knowledge.
- No rules.
- No logic.

Just let the data decide the next move.

The results are... surprisingly mixed.

Sometimes the model makes a perfect move, and sometimes it confidently recommends a move that loses immediately. Why? Because our dataset contains every legal game, including the terrible ones. The model learns human decisions—not necessarily good decisions.

<a href="simple_baseline_move_predictor/DESC.md">Check Simple baseline move predictor Documentation</a>

## Rule based predictor

After seeing those mistakes, it became obvious that the dataset alone isn't enough.

So we start teaching the predictor some actual Tic Tac Toe strategy.

Things like:

- Win immediately if possible.
- Block an opponent's immediate win.

Now the predictor isn't only learning from data—it also understands a little bit about the game itself.

<a href="rule_based_predictor/DESC.md">Check rule based predictor Documentation</a>

## Hybrid predictor

The baseline predictor was a good start, but it had one major weakness:

It learned from every legal game, including the bad ones.

So instead of replacing the model, we asked a different question:

`What if we keep the predictor, but only step in when game knowledge clearly knows better?`

This stage combines the simple data-based predictor with a small set of Tic Tac Toe rules. The prediction flow becomes:
- Immediate win?
    ✓ Yes → Take it.
- Otherwise, opponent can win next move?
    ✓ Yes → Block it.
- Otherwise...
    → Use the baseline predictor.

In other words, the predictor still does most of the work, while the rules act as a safety net to prevent obvious mistakes.

This hybrid approach keeps the model simple, but makes its decisions much closer to how an experienced player would actually play.