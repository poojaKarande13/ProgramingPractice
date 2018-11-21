'''
Given directed edges of a graph, topologically sort the elements in the graph
num =  number of nodes in the graph
0 to num-1 nodes
'''
def bfs(graph, visited, num, i):
    visited[i] = -1
    print("visiting ", i)
    for j in graph[i]:
        if visited[j] == -1:
            return False
        elif visited[j] == 0:
            ret = bfs(graph, visited, num, j)
            if ret == False:
                return False
    visited[i] = 1
    print(i)
    return True

def topologicallySort(num, dep):
    graph = [[] for _ in range(num)]
    visited = [0] * num
    # 0   not visited
    # -1  traversing
    # 1   visited
    for x, y in dep:
        graph[x].append(y)

    for i in range(num):
        if visited[i] !=  1:
            res = bfs(graph, visited, num, i)
            if res == False:
                return res

print(topologicallySort(6, [[0,1],[5,1],[2,1],[3,2],[4,2]]))
