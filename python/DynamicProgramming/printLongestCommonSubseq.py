
def printLongestSubseq(X, Y):
    n = len(X)
    m = len(Y)
    res = []
    T = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if X[i] == Y[j]:
                prev = T[i-1][j-1] if i >= 0 and j>0 else 0
                T[i][j] = prev + 1
                if prev == 0:
                    res.append(X[i])
                else:
                    res1 = []
                    for s in res:
                        res1.append(s+X[i])
                    res = res1
            else:
                x = T[i-1][j] if i > 0 else 0
                y = T[i][j-1] if j > 0 else 0
                T[i][j] = max(x, y)
    print(T)
    print(res)

printLongestSubseq('ABCBDAB','BDCABA')
