def interleave(A,B,C):
    m = len(A)
    n = len(B)

    if m+n != len(C):
        return False

    if len(C) == 0:
        return True


    M = [[0 for i in range(n+1)] for j in range(m+1)]

    M[0][0] = 1

    for i in range(m+1):
        for j in range(n+1):
            k = i+j-1

            if i == 0 and j == 0:
                M[i][j] = 1
            elif i == 0 and B[j-1] == C[k]:
                M[i][j] = M[i][j-1]
            elif j == 0 and A[i-1] == C[k]:
                M[i][j] = M[i-1][j]
            elif B[j-1] != C[k] and A[i-1] == C[k]:
                M[i][j] = M[i-1][j]
            elif B[j-1] == C[k] and A[i-1] != C[k]:
                M[i][j] = M[i][j-1]
            elif B[j-1] == C[k] and A[i-1] == C[k]:
                M[i][j] = M[i][j-1] or  M[i-1][j]
            else:
                M[i][j] = 0

    return M[-1][-1] == 1

print(interleave("aabcc", "dbbca" , "aadbbbaccc"))
