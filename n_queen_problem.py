def is_safe(board, row, col, n):
    for i in range(row):
        if board[i][col] == 1:
            return False
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    i, j = row, col
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True

def solve_n_queens(board, row, n, solutions):
    if row == n:
        solutions.append([row[:] for row in board])
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve_n_queens(board, row + 1, n, solutions)
            board[row][col] = 0

def print_solutions(solutions):
    if not solutions:
        print("No solutions found.")
    for sol in solutions:
        for row in sol:
            print(" ".join("Q" if cell else "." for cell in row))
        print()

n = 4
board = [[0 for _ in range(n)] for _ in range(n)]
solutions = []
solve_n_queens(board, 0, n, solutions)
print_solutions(solutions)