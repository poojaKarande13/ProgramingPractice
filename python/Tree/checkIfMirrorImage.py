'''
Write code in Java to find out whether a binary tree is a mirror image of itself or not. Should code be thread-safe?

            a
        b       b
    c      d  d     c
1     2  4  5 5 4  2   1

'''
import queue
class Node:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

def checkIfMirror(root):
    leftQueue =  queue.Queue()
    rightQueue =  queue.Queue()

    left = root.left
    right = root.right

    while left != None and right != None and left.val == right.val:
        leftQueue.put(left.left)
        leftQueue.put(left.right)
        rightQueue.put(right.right)
        rightQueue.put(right.left)

        left = leftQueue.get()
        right = rightQueue.get()

    if leftQueue.qsize() != rightQueue.qsize():
        return False
    if left != right and left.val != right.val:
        return False
    return True

root = Node('a')
root.left = Node('b')
root.right = Node('b')

root.left.left = Node('c')
root.left.right = Node('d')

root.right.right = Node("c")
root.right.left = Node("dz")

print(checkIfMirror(root))
