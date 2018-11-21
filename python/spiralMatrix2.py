import math

def circularPrint(matrix, r, c, R, C, result, visited, mR, mC):
    R = R + r
    C = C + c
    for j in range(c,C):
        if r < mR and j < mC and visited[r][j] == 0:
            result.append(matrix[r][j])
            visited[r][j] = 1

    for i in range(r+1,R):
        if visited[i][C-1] == 0:
            result.append(matrix[i][C-1])
            visited[i][C-1] = 1

    for j in range(C-2, c-1, -1):
        if visited[R-1][j] == 0:
            result.append(matrix[R-1][j])
            visited[R-1][j] = 1

    for i in range(R-2,r,-1):
        if visited[i][c] == 0:
            result.append(matrix[i][c])
            visited[i][c] = 1

def spiralOrder(matrix):
    R = len(matrix)
    res = []
    if R == 0:
        return res
    C = len(matrix[0])
    visited = [[0 for _ in range(C)] for _ in range(R)]
    r = R
    c = C
    for i in range(math.ceil(R/2)):
        print(i)
        circularPrint(matrix, i, i, r, c, res, visited, mR, mC)
        r -= 2
        c -= 2
    return res

print(spiralOrder([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]]))
