# Simple baseline move predictor
This predictor will predict best move for player in each state of game based on dataset datas.
### Step 1
First, we create a test case to see how dataset works. If needed, we will make some rules to make our model smarter.

Test is simple. I want to see what is the best move for player two after this situation:
<table>
<tr><td></td><td>0</td><td>1</td><td>2</td></tr>
<tr><td>0</td><td>O</td><td>-</td><td>-</td></tr>
<tr><td>1</td><td>-</td><td>X</td><td>X</td></tr>
<tr><td>2</td><td>-</td><td>-</td><td>-</td></tr>
</table>

The model have to suggest move 1-0, otherwise it is not smart enough to help win the game.

Result is not what I expected:
```
Move 0-1 -> Win Rate: 37.70% | Draw Rate: 0.00% | Lose Rate: 37.70%
Move 0-2 -> Win Rate: 34.33% | Draw Rate: 17.91% | Lose Rate: 16.42%
Move 2-0 -> Win Rate: 49.12% | Draw Rate: 0.00% | Lose Rate: 49.12%
Move 2-1 -> Win Rate: 21.92% | Draw Rate: 16.44% | Lose Rate: 5.48%
Move 2-2 -> Win Rate: 21.92% | Draw Rate: 0.00% | Lose Rate: 21.92%
Move 1-0 -> Win Rate: 37.21% | Draw Rate: 13.95% | Lose Rate: 23.26%
```

Unfortunately, model suggests to move 2-0 which is an absolute lose. Based on low lose rate, model suggests to move 2-1 which is an another absolute lose too. 

As you see, there is no any sign or strategy in results to make a fact based on that. This is because our dataset is not created by people experiences but by covering every possible moves. So as usually expect a well-minded human move 1-0, someone who are less-minded could make different decisions and lose.

In the next-step, we will improve our predictor by adding rules and game knowledges, such as detecting immediate wins or preventing another player from wining.