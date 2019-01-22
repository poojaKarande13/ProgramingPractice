
def track(mat, row, position, n):
    if row == n:
        return True
    for col in range(len(mat)):
        # check if column col has any queens or check diagonal
        if col in position and (position[col][1] == col or position[col][0] == row or (position[col][0] - position[col][1]) == (row - col) or  (position[col][0] + position[col][1]) == (row + col) ):
            continue
        else:
            mat[col][row] = "Q"
            position[col] = (row, col)
            if track(mat, row+1, position, n) == True:
                return True
            del position[col]
            mat[col][i] = "."

    return False

def solveNQueens(n):
    res = []
    row = 0

    for col in range(n):
        mat = [["." for i in range(n)] for j in range(n)]
        position = {}
        mat[col][row] = "Q"
        position[col] = (row, col)
        if track(mat, row+1, position, n) == True:
            res.append(mat)

    return res

print(solveNQueens(4))
