def findMinHeightTrees(n, edges):
    """
    :type n: int
    :type edges: List[List[int]]
    :rtype: List[int]
    """
    if n < 3:
        return list(range(n))

    # create adj matrix
    adj = [[] for i in range(n)]

    for i, j in edges:
        adj[i].append(j)
        adj[j].append(i)

    leaves = [ i for i in range(n) if len(adj[i]) == 1 ]
    while n > 2:
        n -= len(leaves)
        new_leaves = []
        for leave in leaves:
            # remove parent from leave node
            j = adj[leave][0]
            # remove link of leave node from parent
            adj[j].remove(leave)
            #make parent leave if parent has degree 1
            if len(adj[j]) == 1:
                new_leaves.append(j)
        leaves = new_leaves

    return leaves

print(findMinHeightTrees(4,[[1, 0], [1, 2], [1, 3]]))
print(findMinHeightTrees(6,[[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]))
