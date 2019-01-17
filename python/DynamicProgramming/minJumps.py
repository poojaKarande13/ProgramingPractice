import sys
def getMinJumps(A):
    n = len(A)
    if n < 2:
        return 0

    L = [0 for i in range(n)]
    L[n-1] = 0
    for k in range(n-2, -1, -1):
        ans = sys.maxint
        for s in range(1,A[k]+1):
            if k+s < n:
                ans = min(ans, L[k+s])

        L[k] = ans + 1


    if L[0] == sys.maxint+1:
        return -1
    return L[0]

print(getMinJumps([3,3,1,2,2,0]))
