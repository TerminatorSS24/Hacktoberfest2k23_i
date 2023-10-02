def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        row = int(input(f"Player {player}, enter row (0, 1, or 2): "))
        col = int(input(f"Player {player}, enter column (0, 1, or 2): "))

        if board[row][col] != " ":
            print("That spot is already taken. Try again.")
            continue

        board[row][col] = player
        print_board(board)

        if check_winner(board, player):
            print(f"Player {player} wins! Congratulations!")
            break

        if is_board_full(board):
            print("It's a tie!")
            break

        player = "O" if player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()
