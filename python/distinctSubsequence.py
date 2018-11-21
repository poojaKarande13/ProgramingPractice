def distinctSubseqII(S):
    dp = [1]
    last = {}
    for i, x in enumerate(S):
        print(last, dp)
        dp.append(dp[-1] * 2)
        if x in last:
            dp[-1] -= dp[last[x]]
        last[x] = i

    return (dp[-1] - 1) % (10**9 + 7)

print(distinctSubseqII('aa'))
