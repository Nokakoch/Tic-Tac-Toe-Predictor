def create_board(moves):
    board = [["-" for _ in range(3)] for _ in range(3)]
    for i, move in enumerate(moves):
        row, col = map(int, move.split("-"))
        board[row][col] = "X" if i%2 == 0 else "O"
    return board

def is_winner(board,player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for row in board:
        if all(row[col] == player for col in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def find_winning_move(board, player):
    for row in range(3):
        for col in range(3):
            if(board[row][col] != "-"):
                continue
            
            board[row][col] = player
            if is_winner(board,player):
                return f"{row}-{col}"
            board[row][col] = "-"

def find_blocking_move(board, player):
    opponent = "O" if player == "X" else "X"
    return find_winning_move(board,opponent)

moves = input("Enter moves(row-col) seperate with ',':\n").split(',')
board = create_board(moves)
print(board)
player = "X" if len(moves)%2 == 0 else "O"
print(find_blocking_move(board,player))