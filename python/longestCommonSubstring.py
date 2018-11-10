def longestCommonSubstring(str1, str2):
    m = len(str1)
    n = len(str2)
    table = [[0 for _ in range(m)] for __ in range(n)]

    maxLen = 0

    for i in range(n):
        for j in range(m):
            if str2[i] == str1[j]:
                x = table[i-1][j-1] if i-1>=0 and j-1>=0 else 0
                table[i][j] = 1 + x
                maxLen = max(maxLen, table[i][j])
    return maxLen

print(longestCommonSubstring('OldSite:GeeksforGeeks.org', 'NewSite:GeeksQuiz.com'))
