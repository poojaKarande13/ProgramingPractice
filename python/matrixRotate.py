
# rotate matrix anti clockwise by 90 degrees
def rotateMatrix(matrix):
    N = len(matrix)

    i = 0
    j = 0

    for i in range(N):
        row = ""
        for j in range(N):
            row = row + str(matrix[i][j]) + " "
        print(row,"\n")

    for x in range(0, int(N/2)):
        for y in range(x,N-x-1):
            print(x,y,N-y-1)
            t = matrix[x][y]
            matrix[x][y] = matrix[y][N-x-1]
            matrix[y][N-x-1] = matrix[N-x-1][N-y-1]
            matrix[N-x-1][N-y-1] = matrix[N-y-1][x]
            matrix[N-y-1][x] = t

    print("\n\n----")
    for i in range(N):
        row = ""
        for j in range(N):
            row = row + str(matrix[i][j]) + " "
        print(row,"\n")

rotateMatrix([[1,2,3],[4,5,6],[7,8,9]])
