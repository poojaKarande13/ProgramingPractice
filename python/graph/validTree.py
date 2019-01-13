# Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes),
# write a function to check whether these edges make up a valid tree.
#
# For example:
#
# Given n = 5 and edges = [[0, 1], [0, 2], [0, 3], [1, 4]], return true.
#
# Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], return false.

def DFS(node, adjMat, visited):
    if visited[node] != 0:
        return False

    # mark as visiting
    visited[node] = -1

    # for each neighbour of node perform DFS
    for j in adjMat[node]:
        if DFS(j, adjMat, visited) ==  False:
            return False

    visited[node] = 1
    return True

def validTree(edges, n):
    adjMat = [[] for i in range(n)]

    for u, v in edges:
        adjMat[u].append(v)

    visited = [0 for i in range(n)]

    for node in range(n):
        if visited[node] == 0:
            if DFS(node, adjMat, visited) == False:
                return False

    return True

print(validTree([[0, 1], [0, 2], [0, 3], [1, 4]], 5))
print(validTree([[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], 5))
