import sys

def matrixChainMulti(arr):
    n = len(arr)

    m = [[-1 for i in range(n)] for i in range(n)]

    for i in range(n):
        m[i][i] = 0

    for L in range(2,n):
        for i in range(1, n - L + 1):
            j = L + i - 1
            print(L, i, j)
            m[i][j] = sys.maxint
            for k in range(i, j):

                q = m[i][k] + m[k+1][j] + arr[i-1]*arr[k]*arr[j]

                print(q, m[i][k], m[k+1][j], arr[i-1]*arr[k]*arr[j])

                if q < m[i][j]:
                    m[i][j] = q

    print(m)
print(matrixChainMulti([40, 20, 30, 10, 30]))
