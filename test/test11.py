def is_safe(board, row, col, n):
    for i in range(row):
        if board[i][col] == 'Q':
            return False
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1
    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1
    return True

def print_board(board, n):
    for i in range(n):
        print(' '.join(board[i]))
    print()

def solve_n_queens(board, row, n, solutions):
    if row == n:
        solutions.append([row[:] for row in board])
        return
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 'Q'
            solve_n_queens(board, row + 1, n, solutions)
            board[row][col] = '.'

def n_queens(n):
    if n <= 0:
        print("None")
        return
    board = [['.' for _ in range(n)] for _ in range(n)]
    solutions = []
    solve_n_queens(board, 0, n, solutions)
    if not solutions:
        print("None")
    else:
        for solution in solutions:
            print_board(solution, n)

n = int(input())
n_queens(n)