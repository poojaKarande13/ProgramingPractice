class Node:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

class LLNode:
    def __init__(self, data):
        self.val = data
        self.front = None
        self.back = None

def convert(root):
    if root == None:
        return None,None

    bnode1, bnode2 = convert(root.left)
    fnode1, fnode2 = convert(root.right)

    node = LLNode(root.val)
    if bnode1 == None:
        head = node
    else:
        head = bnode1
        bnode2.front = node
        node.back = bnode2

    if fnode2 == None:
        tail = node
    else:
        tail = fnode2
        fnode1.back = node
        node.front = fnode1

    return head, tail

def convertTreeToDll(root):
    root, tail = convert(root)
    while root != None:
        print(root.val)
        root = root.front

root = Node(12)
root.left = Node(10)
root.right = Node(20)
root.right.left = Node(25)
root.right.right = Node(40)

convertTreeToDll(root)
