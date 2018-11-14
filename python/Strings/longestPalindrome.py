def longestPalindrome(my_string):
    n = len(my_string)
    maxLen = 1

    mat = [1] * n

    # for len = 2
    for i in range(1,n):
        mat[i] = 2 if my_string[i] == my_string[i-1] else 1

    print(mat)
    # for len 3 to N
    for i in range(2,n):
        for j in range(i,n):
            print(i,j,mat[j-1], my_string[j], my_string[j-i])
            if mat[j-1] == (i/2) and my_string[j] == my_string[j-i]:
                print("incr")
                mat[j] = i
                maxLen = max(maxLen, mat[j])
    print(mat)
    return maxLen

print(longestPalindrome("abcba"))
