import sys
def minimumCutPalindrome(a):
    n = len(a)

    if n < 2:
        return 0

    L = [[0 for i in range(n)] for i in range(n)]
    c = [[0 for i in range(n)] for i in range(n)]
    # mark all length 1 palindrome
    for i in range(n):
        L[i][i] = 1

    #length wise iterate over matrix and find palindrome length
    for cl in range(2, n+1):
        for i in range(0, n - cl):
            j = i + cl - 1
            if a[i] == a[j]:
                if cl == 2:
                    L[i][j] = 1
                else:
                    if L[i+1][j-1] == 1:
                        L[i][j] = 1

            if L[i][j] == 1:
                c[i][j] = 0
            else:
                c[i][j] = sys.maxint
                for k in range(i,j):
                    c[i][j] = min(c[i][j] ,
                                c[i][k] + c[k+1][j+1] + 1)

    for i in range(len(c)):
        print(c[i])

minimumCutPalindrome("abcde")


    # L[i][j] = length of palindrome starting at i and of length j
    #
    # for cl in range(n, -1, -1):
    #     for i in range(0, n-cl):
    #         j = i+cl-1
    #
    #         # check if there is a palindrome starting at i
    #         if L[i][j] != 0:

    # for i in range(n):
    #     print(L[i])
    #
    # C = [sys.maxint for i in range(n)]
    #
    # for i in range(n):
    #     if L[0][i] > 0:
    #         C[i] = 0
    #     else:
    #         for j in range(i):
    #             if L[j+1][i] > 0 and C[i] > 1 + C[j]:
    #                 C[i] = 1 + C[j]
    # print("\n")
