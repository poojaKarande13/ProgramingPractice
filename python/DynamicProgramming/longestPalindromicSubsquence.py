def longestPalindrome(str):

    n = len(str)

    if n < 2:
        return str

    L = [[0 for i in range(n)] for i in range(n)]

    for i in range(n):
        L[i][i] = 1

    maxNum = 1

    for cl in range(2,n+1):
        for i in range(n-cl+1):
            j = i + cl -1
            if str[i] == str[j] and cl == 2:
                L[i][j] = cl
            elif str[i] == str[j]:
                L[i][j] = L[i+1][j-1] + 2
            else:
                L[i][j] = max(L[i][j-1], L[i+1][j])
            maxNum = max(maxNum, L[i][j])

    print(L)
    return maxNum

print(longestPalindrome("geekees"))
