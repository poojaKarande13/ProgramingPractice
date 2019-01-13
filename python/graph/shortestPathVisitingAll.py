import collections
def shortestPathVisitingAll(graph):
    N = len(graph)
    queue = collections.deque((1 << x, x) for x in xrange(N))
    print('queue', queue)
    dist = collections.defaultdict(lambda: N*N)
    print('dist', dist)
    for x in xrange(N): dist[1 << x, x] = 0
    print('dist', dist)

    while queue:
        cover, head = queue.popleft()
        d = dist[cover, head]
        if cover == 2**N - 1: return d
        for child in graph[head]:
            cover2 = cover | (1 << child)
            if d + 1 < dist[cover2, child]:
                dist[cover2, child] = d + 1
                queue.append((cover2, child))

    print(queue)
    print(dist)

print(shortestPathVisitingAll([[1,2,3],[0],[0],[0]]))



#[[1],[0,2,4],[1,3,4],[2],[1,2]]
