def editDistance(A, B):
    n = len(A)
    m = len(B)
    if A == B:
        return 0
    D =[ [0 for i in range(m + 1)] for j in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, m+1):
            if A[i-1] == B[j-1]:
                D[i][j] = D[i-1][j-1]
            else:
                D[i][j] = min(D[i][j-1], D[i-1][j], D[i-1][j-1]) + 1

    return D[-1][-1]

print(editDistance('Anshuman', 'Anithuman'))
