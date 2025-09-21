import numpy as np

board = np.full((3, 3), ' ')
turn = 'X'


def show_board():
    print("\n".join(["|".join(row) for row in board]))


def winner():
    return any(np.all(board[i, :] == turn) or np.all(board[:, i] == turn) for i in range(3)) or np.all(np.diag(board) == turn)


while True:
    show_board()
    move = input(f"Move {turn} (0-8): ")

    if move.isdigit() and int(move) in range(9):
        row, col = divmod(int(move), 3)
        if board[row, col] == ' ':
            board[row, col] = turn


            if winner():
                show_board()
                print(f"Winner: {turn}")
                break
            if not np.any(board == ' '):
                show_board()
                print("Draw!")
                break

            turn = 'O' if turn == 'X' else 'X'
