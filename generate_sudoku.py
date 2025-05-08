import random
from solve_sudoku import solve_sudoku

def generate_sudoku():
    def fill_board(board):
        def fill_box(start_row, start_col):
            numbers = list(range(1, 10))
            random.shuffle(numbers)
            for i in range(3):
                for j in range(3):
                    board[start_row + i][start_col + j] = numbers.pop()

        for i in range(0, 9, 3):
            fill_box(i, i)

        solve_sudoku(board)

    def remove_numbers(board, difficulty=40):
        attempts = difficulty
        while attempts > 0:
            row = random.randint(0, 8)
            col = random.randint(0, 8)
            if board[row][col] != 0:
                board[row][col] = 0
                attempts -= 1

    board = [[0 for _ in range(9)] for _ in range(9)]
    fill_board(board)
    remove_numbers(board, 40)

    return board
