# In this coding sample, I was given 90 minutes to answer 2 coding questions.
#
# Question 1: Given a string A consisting of n characters and a string B consisting of m characters, write a function that will return the number of times A must be stated such that B is a substring of the repeated A. If B can never be a substring, return -1.
#
# Example:
# A = abcd
# B = cdabcdab
# The function should return 3 because after stating A 3 times, getting abcdabcdabcd, B is now a substring of A.
#
# You can assume that n and m are integers in the range [1, 1000].

def func(A, B):
    N = len(A)
    M = len(B)

    mat = [[0 for i in range(N)] for j in range(M)]
    count = 0
    for i in range(M):
        for j in range(N):
            if A[j] == B[i]:
                if i == 0:
                    mat[i][j] = 1
                    count = 1
                elif j == 0:
                    mat[i][j] = mat[i-1][-1] + 1
                    count += 1
                else:
                    if mat[i-1][j-1] == 0:
                        return -1
                    else:
                        mat[i][j] = mat[i-1][j-1]

    return count

print(func('abcd','cdabcdabcdab'))
