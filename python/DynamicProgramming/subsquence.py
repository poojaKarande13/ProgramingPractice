# def findCount(S, T):
#     n = len(S)
#     m = len(T)
#
#     if m > n:
#         return 0
#
#     mat = [[ 0 for j in range(m+1)] for i in range(n+1)]
#
#     for i in range(n+1):
#         mat[i][0] = 1
#
#     for j in range(1, m+1):  # t
#         for i in range(1, n+1): # s
#             if S[i-1] == T[j-1]:
#                 mat[i][j] = mat[i-1][j] + mat[i-1][j-1]
#             else:
#                 mat[i][j] = mat[i-1][j]
#
#     print(mat)
#
#     return mat[n][m]

def findCount(S, T):
    n = len(S)
    m = len(T)

    if m > n:
        return 0

    mat = [[0 for j in range(m+1)] for i in range(n+1)]

    for i in range(n+1):
        mat[i][0] = 1

    for j in range(1, m+1):
        for i in range(1, n+1):
            if S[i-1] == T[j-1]:
                mat[i][j] = mat[i-1][j-1] + mat[i-1][j]
            else:
                mat[i][j] = mat[i-1][j]

    print(mat)
    return mat[-1][-1]


print(findCount("rabbbit","rabbit"))


# def findCount(s, t):
#     l_s, l_t = len(s), len(t)
#     if l_s < l_t: return 0
#
#     dp = [[0] * (l_s + 1) for _ in range(l_t + 1)]
#     dp[0] = [1] * (l_s + 1)
#
#     for i in range(1, l_t + 1):
#         for j in range(1, l_s + 1):
#             if s[j - 1] == t[i - 1]:
#                 dp[i][j] = dp[i][j-1] + dp[i-1][j-1]
#             else:
#                 dp[i][j] = dp[i][j-1]
#     return dp[-1][-1]
#
# print(findCount("rabbbit","rabbit"))
