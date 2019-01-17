import sys
def minimumPalindromeCut(a):
    n = len(a)

    if n < 2:
        return 0

    c = [[0 for i in range(n)] for i in range(n)]

    for i in range(n):
        c[i][i] = 0

    for l in range(2, n+1):
        for i in range(n-l+1):
            j = i+l-1

            if l == 2:
                if a[i] == a[j]:
                    c[i][j] = 0
                else:
                    c[i][j] = 1
            else:
                if a[i] == a[j] and c[i+1][j-1] == 0:
                    c[i][j] = 0
                else:
                    # if string from a[i] to a[j] is not a palindrome

                    # cut the string into k parts and find minimum number of cuts
                    c[i][j] = sys.maxint
                    for k in range(i,j-1):
                        print(a[i:k], a[k+1:j])
                        c[i][j] = min(c[i][j], 1 + c[i][k] + c[k+1][j])

    for i in range(n):
        print(c[i])
    print(c[0][n-1])
minimumPalindromeCut("abcbaasd")











#
