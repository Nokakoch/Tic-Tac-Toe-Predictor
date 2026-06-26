import pandas as pd

dataset = pd.read_csv("tictactoe_games.csv")

moves = ["1-1","0-0","1-2"]
filtered = dataset.copy()

for i,m in enumerate(moves):
    player = "X" if i%2 == 0 else "O"
    col = f"Move {i+1}-{player} (Row-Col)"
    filtered = filtered[filtered[col]==m]

next_move_number = len(moves)
next_move_player = "X" if next_move_number % 2 == 0 else "O"
next_column = f"Move {next_move_number + 1}-{next_move_player} (Row-Col)"
possible_moves = filtered[next_column].dropna().unique()


for next_move in possible_moves:
    move_data = filtered[filtered[next_column]==next_move]
    total = len(move_data)
    wins = len(move_data[ move_data["Winner"] == next_move_player])
    draws = len(move_data[move_data["Winner"] == "-"])
    loses = wins - draws

    win_rate = wins / total * 100
    draw_rate = draws / total * 100
    lose_rate = loses / total * 100
    print(f"Move {next_move} -> Win Rate: {win_rate:.2f}% | Draw Rate: {draw_rate:.2f}% | Lose Rate: {lose_rate:.2f}%")