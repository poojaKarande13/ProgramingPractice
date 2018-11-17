import queue

t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    # R is runs
    # k is capacity
    # N no of groups
    R, k, N = [int(s) for s in input().split(" ")]
    q =  input().split(" ")
    memo = [0] * N
    for j in range(N):
        n = j
        sizeOfRun = 0
        flag = True
        while flag == True:
            if (int(q[n]) + sizeOfRun) <= k:
                sizeOfRun += int(q[n])
                new = n + 1 if n != N-1 else 0
                if n == new or j == new:
                    flag = False
                n = new
            else:
                flag = False
        memo[j] = (sizeOfRun, n)

    revenue = 0
    ptr = 0
    #print(q)
    #print(memo)
    for _ in range(R):
        revenue += memo[ptr][0]
        ptr = memo[ptr][1]


    print("Case #{}: {}".format(i, revenue))
