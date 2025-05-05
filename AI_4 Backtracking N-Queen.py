def is_safe(board, row, col, n):
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, n), range(col, -1, -1)):
        if i < n and board[i][j] == 1:
            return False

    return True


def solve_n_queens_bt(board, col, n):
    if col >= n:
        return True

    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            if solve_n_queens_bt(board, col + 1, n):
                return True
            board[i][col] = 0  

    return False

def print_solution(board, n):
    for i in range(n):
        for j in range(n):
            print("Q" if board[i][j] else ".", end=" ")
        print()

n = 8
board = [[0] * n for _ in range(n)]

if solve_n_queens_bt(board, 0, n):
    print("Solution using Backtracking:")
    print_solution(board, n)
else:
    print("No solution exists.")


def solve_n_queens_bb(col, n, board, row_lookup, slash_lookup, backslash_lookup, slash_code, backslash_code):
    if col >= n:
        return True

    for i in range(n):
        if not row_lookup[i] and not slash_lookup[slash_code[i][col]] and not backslash_lookup[backslash_code[i][col]]:
            board[i][col] = 1
            row_lookup[i] = True
            slash_lookup[slash_code[i][col]] = True
            backslash_lookup[backslash_code[i][col]] = True

            if solve_n_queens_bb(col + 1, n, board, row_lookup, slash_lookup, backslash_lookup, slash_code, backslash_code):
                return True

            board[i][col] = 0
            row_lookup[i] = False
            slash_lookup[slash_code[i][col]] = False
            backslash_lookup[backslash_code[i][col]] = False

    return False


n = 8
board = [[0] * n for _ in range(n)]

slash_code = [[0] * n for _ in range(n)]
backslash_code = [[0] * n for _ in range(n)]
for r in range(n):
    for c in range(n):
        slash_code[r][c] = r + c
        backslash_code[r][c] = r - c + (n - 1)

row_lookup = [False] * n
slash_lookup = [False] * (2 * n - 1)
backslash_lookup = [False] * (2 * n - 1)

if solve_n_queens_bb(0, n, board, row_lookup, slash_lookup, backslash_lookup, slash_code, backslash_code):
    print("\nSolution using Branch and Bound:")
    print_solution(board, n)
else:
    print("No solution exists.")


