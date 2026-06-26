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