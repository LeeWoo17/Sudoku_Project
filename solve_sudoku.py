def solve_sudoku(board):
    def find_empty_cell(board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    return i, j
        return None

    def is_valid_move(board, row, col, num):
        if num in board[row]:
            return False
        if num in [board[i][col] for i in range(9)]:
            return False
        box_row_start = (row // 3) * 3
        box_col_start = (col // 3) * 3
        for i in range(3):
            for j in range(3):
                if board[box_row_start + i][box_col_start + j] == num:
                    return False
        return True

    empty_cell = find_empty_cell(board)
    if not empty_cell:
        return board

    row, col = empty_cell
    for num in range(1, 10):
        if is_valid_move(board, row, col, num):
            board[row][col] = num
            if solve_sudoku(board):
                return board
            board[row][col] = 0

    return None
