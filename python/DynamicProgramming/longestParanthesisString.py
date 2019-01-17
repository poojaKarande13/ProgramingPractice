def longest(s):
    n = len(s)
    if n < 2:
        return 0

    dp = [0 for i in range(n)]

    maxLen = 0

    for i in range(1,n):
        if s[i] == ')':
            if s[i] == '(':
                dp[i] = dp[i-2] + 2
            else:
                k = i - dp[i-1] - 1
                if k>=0 and s[k] == '(':
                    dp[i] = dp[i-1] + 2 + dp[i - dp[i-2] - 2]

        maxLen = max(maxLen, dp[i])

    print(dp)

    return maxLen

print(longest("))))))"))
