INT_MAX = 1000
def selectMin(vertices, distance):
    min = vertices[0]
    for v in vertices:
        if distance[min] > distance[v]:
            min = v
    return min

def dijkstra(graph, source, N):
    #create adj matrix
    adjMat = [[INT_MAX for i in range(N)] for i in range(N)]

    for u, v, d in graph:
        adjMat[u][v] = d

    vertices = [i for i in range(N)]

    distance = [INT_MAX for i in range(N)]
    distance[source] = 0
    vertices.remove(source)

    for i in range(N):
        if distance[i] > adjMat[source][i]:
            distance[i] = adjMat[source][i]

    while vertices:
        # min node with minimum distance from source and also not selected before
        selected = selectMin(vertices, distance)
        vertices.remove(selected)
        for v in range(N):
            if v in vertices and distance[v] > (distance[selected] + adjMat[selected][v]):
                distance[v] = distance[selected] + adjMat[selected][v]


    return distance

print(dijkstra([[0,1,50], [1,3,15], [4,1,20], [3,4,15],[0,3,10],[3,0,10],[0,2,45],[5,4,3],[2,4,30],[4,1,20],[4,2,35]], 0, 6))
