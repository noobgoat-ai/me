
N = 8

board = [-1] * N

# Check whether position is safe
def is_safe(row, col):

    for i in range(row):

        if board[i] == col:
            return False

        if abs(board[i] - col) == abs(i - row):
            return False

    return True


# Backtracking function
def solve(row):

    if row == N:
        return True

    for col in range(N):

        if is_safe(row, col):

            board[row] = col

            if solve(row + 1):
                return True

            board[row] = -1

    return False


# Solve problem
if solve(0):

    print("Solution Found!")

    for row in range(N):
        for col in range(N):

            if board[row] == col:
                print("Q", end=" ")
            else:
                print(".", end=" ")

        print()

    print("Queen Positions:", [x + 1 for x in board])

else:
    print("No solution found")
