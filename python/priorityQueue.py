class priorityQueue:
    def __init__(self):
        self.queue = []

    def add(self, priority, elem):
        self.queue.append((priority, elem))

    def remove(self):
        if len(self.queue) != 0:
            self.queue.sort(reverse=True)
            return self.queue.pop()
        else:
            return None
    def isEmpty(self):
        return len(self.queue) == 0

q = priorityQueue()
q.add(10,6)
q.add(1,4)
q.add(7,5)
q.add(5,3)

while q.isEmpty() != True:
    print(q.remove())
