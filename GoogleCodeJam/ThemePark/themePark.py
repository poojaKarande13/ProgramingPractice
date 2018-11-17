import queue

t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    # R is runs
    # k is capacity
    # N no of groups
    R, k, N = [int(s) for s in input().split(" ")]
    q = queue.Queue()

    for elem in input().split(" "):
        q.put(elem)

    revenue = 0
    # for each run
    for _ in range(R):
        sizeOfRun = 0
        runGrps = []
        while q.qsize() != 0 and (sizeOfRun + int(q.queue[0])) <= k:
            grpSize = int(q.get())
            sizeOfRun += grpSize
            runGrps.append(grpSize)
        for g in runGrps:
            q.put(g)
        revenue += sizeOfRun

    print("Case #{}: {}".format(i, revenue))
