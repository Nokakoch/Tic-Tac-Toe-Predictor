import pandas as pd
dataset = pd.read_csv("tictactoe_games.csv")


def create_board(moves):
    board = [["-" for _ in range(3)] for _ in range(3)]

    for i, move in enumerate(moves):
        row, col = map(int, move.split("-"))
        board[row][col] = "X" if i % 2 == 0 else "O"

    return board


def print_board(board):
    print()
    print("  0 1 2")
    for i, row in enumerate(board):
        print(i, " ".join(row))
    print()


def is_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)):
        return True

    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def find_winning_move(board, player):
    for row in range(3):
        for col in range(3):
            if board[row][col] != "-":
                continue

            board[row][col] = player

            if is_winner(board, player):
                board[row][col] = "-"
                return f"{row}-{col}"

            board[row][col] = "-"

    return None


def find_blocking_move(board, player):
    opponent = "O" if player == "X" else "X"
    return find_winning_move(board, opponent)


def filter_dataset(dataset, moves):

    filtered = dataset.copy()

    for i, move in enumerate(moves):
        player = "X" if i % 2 == 0 else "O"
        column = f"Move {i+1}-{player} (Row-Col)"
        filtered = filtered[filtered[column] == move]

    return filtered


def predict_by_dataset(dataset, moves):

    filtered = filter_dataset(dataset, moves)

    next_move_number = len(moves)
    player = "X" if next_move_number % 2 == 0 else "O"

    column = f"Move {next_move_number+1}-{player} (Row-Col)"

    if column not in filtered.columns:
        return

    possible_moves = filtered[column].dropna().unique()

    if len(possible_moves) == 0:
        print("No dataset prediction.")
        return

    best_move = None
    best_score = -1

    for move in possible_moves:
        move_data = filtered[filtered[column] == move]
        
        total = len(move_data)
        wins = len(move_data[move_data["Winner"] == player])
        draws = len(move_data[move_data["Winner"] == "-"])
        opponent = "O" if player == "X" else "X"
        loses = len(move_data[move_data["Winner"] == opponent])

        win_rate = wins / total * 100
        draw_rate = draws / total * 100
        lose_rate = loses / total * 100

        print(
            f"Move {move} -> "
            f"Win: {win_rate:.2f}% | "
            f"Draw: {draw_rate:.2f}% | "
            f"Lose: {lose_rate:.2f}%"
        )

        score = win_rate - lose_rate

        if score > best_score:
            best_score = score
            best_move = move

    print(f"\nDataset suggestion: {best_move}")


moves = []

while len(moves) < 9:

    board = create_board(moves)
    player = "X" if len(moves) % 2 == 0 else "O"

    print_board(board)

    move = find_winning_move(board, player)

    if move:
        print(f"-> Immediate win: {move}")

    else:

        move = find_blocking_move(board, player)

        if move:
            print(f"-> Block opponent: {move}")

        else:
            predict_by_dataset(dataset, moves)

    move = input(f"\nPlayer {player}, enter your move (row-col): ")

    moves.append(move)

    board = create_board(moves)

    if is_winner(board, player):
        print_board(board)
        print(f"{player} wins!")
        break

else:
    print_board(create_board(moves))
    print("Draw!")