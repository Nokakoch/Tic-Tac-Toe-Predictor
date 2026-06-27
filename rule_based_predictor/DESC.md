# Rule Based Predictor

There are two main goals in Tic-Tac-Toe: try to win the game, otherwise don't let your opponent win.

The problem with the simple baseline predictor was that it only looked at the win rate of the next move. That works only if the opponent also plays random moves and doesn't try to win.

However, our dataset contains every possible move, not only good moves. So the predictor eventually suggests moves based on all possible moves not the best ones.

In this step, we solve this problem by adding simple game rules, such as detecting immediate winning moves or blocking the opponent's winning move.

## Step 1

Before adding any rules, we need to know what should be checked first. The most important question is:

`Can current player win immediately?`

If there is a winning move, there is no reason to look at dataset statistics or any other rule. The game should end immediately.

```
- Test 1:
-- Input: 
Enter moves(row-col) seperate with ',':
0-0, 1-0, 1-1,1-2
-- Output:
[
    ['X', '-', '-'], 
    ['O', 'X', 'O'], 
    ['-', '-', '-']
]
2-2

- Test 2:
-- Input:
Enter moves(row-col) seperate with ',':
1-1,0-1,2-0,0-2,2-1
-- Output:
[
    ['-', 'O', 'O'],
    ['-', 'X', '-'], 
    ['X', 'X', '-']
]
0-0
```

## Step 2

Sometimes there is no immediate winning move.

In this situation, we should check whether our opponent can win in the next turn. If so, preventing that move becomes the highest priority.

The implementation is almost the same as the previous rule. Instead of simulating our own moves, we simulate every possible move for the opponent. If one of those moves lets the opponent win immediately, we simply play that position ourselves and block it.

This rule has lower priority than the immediate winning rule, because winning the game is always better than anything else. However, it has higher priority than any statistical prediction because losing in the next turn is never acceptable.

Notice that the blocking rule does not require a new algorithm. It just use the winning move detector from the opponent's perspective.

```
- Test 1
-- Input:
Enter moves(row-col) seperate with ',':
1-1,0-1,0-2
- Output:
[
    ['-', 'O', 'X'], 
    ['-', 'X', '-'], 
    ['-', '-', '-']
]
2-0

- Test 2
-- Input:
Enter moves(row-col) seperate with ',':
0-2,0-1,2-0
-- Output:
[
    ['-', 'O', 'X'], 
    ['-', '-', '-'], 
    ['X', '-', '-']
]
1-1
```
