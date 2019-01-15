import sys

def minDistance(word1, word2):
    """
    :type word1: str
    :type word2: str
    :rtype: int
    """
    n1 = len(word1)
    n2 = len(word2)

    if n1 == 0:
        return n2
    if n2 == 0:
        return n1

    mat = [[sys.maxint for i in range(n2)] for i in range(n1)]

    for i in range(n1):
        for j in range(n2):
            if i == 0:
                mat[i][j] = j
            elif j == 0:
                mat[i][j] = i
            elif word1[i] == word2[j]:
                mat[i][j] = mat[i-1][j-1]
            else:
                mat[i][j] = 1 + max(mat[i][j-1], mat[i-1][j], mat[i-1][j-1])

    return mat[n1-1][n2-1]

print(minDistance("se", "at"))
