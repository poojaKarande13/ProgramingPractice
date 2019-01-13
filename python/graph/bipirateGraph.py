'''
Algorithm for bipirate graph

queue = collection.queue - create queue to perform bfs
label = [0] - label to mark groups 0 for no group, 1 and 2

start with 0 and mark at group 1 and insert in queue

while nodes in not empty:
    add node in queue
    give node a color
    while queue is not empty:
        remove u from queue
        for each edge from u to v
            if v have no color:
                give v different color than u and insert v in queue
            if u and v have same color:
                return False
'''
import Queue

def isBipartite(graph):
    N = len(graph)
    label = [-1 for i in range(N)]
    q = Queue.Queue()


    for i in range(len(graph)):
        if label[i] == -1:
            label[i] = 1
            q.put(i)
            while not q.empty():
                u = q.get()
                for v in graph[u]:
                    if label[v] == -1:
                        label[v] = 1 - label[u]
                        q.put(v)
                    elif label[v] == label[u]:
                        return False
    print(label)
    return True

print(isBipartite([[],[2,4,6],[1,4,8,9],[7,8],[1,2,8,9],[6,9],[1,5,7,8,9],[3,6,9],[2,3,4,6,9],[2,4,5,6,7,8]]))
