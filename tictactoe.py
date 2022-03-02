def check_board(board):
    if len(board) != 9:
        return False
    for key, value in board.items():
        if value != "O" and value != "X":
            return False

    return True


def result(board_raw):
    # do not do ["X"]*3, or something similar.
    # python shallow copies the inner lists...

    # TODO: when both X and O wins (invalid state) ?

    board = [["X", "X", "X"], ["X", "X", "X"], ["X", "X", "X"]]
    if not check_board(board_raw):
        return "Invalid board"
    else:
        for i in range(3):
            for j in range(3):
                board[i][j] = board_raw[f"{i} {j}"]

        # rows and columns
        for i in range(3):
            row_sum = 0
            column_sum = 0

            for j in range(3):
                row_sum += ord(board[i][j])
                column_sum += ord(board[j][i])

            if row_sum == (ord("X") * 3) or column_sum == (ord("X") * 3):
                return "X won"
            elif row_sum == (ord("O") * 3) or column_sum == (ord("O") * 3):
                return "O won"

        # diagonals
        diagonal_sum = ord(board[0][0]) + ord(board[1][1]) + ord(board[2][2])
        if diagonal_sum == (ord("X") * 3):
            return "X won"
        elif diagonal_sum == (ord("O") * 3):
            return "O won"

        diagonal_sum = ord(board[0][2]) + ord(board[1][1]) + ord(board[2][0])
        if diagonal_sum == (ord("X") * 3):
            return "X won"
        elif diagonal_sum == (ord("O") * 3):
            return "O won"

        # draw
        return "draw"
