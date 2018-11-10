class Node:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

def commonAncestor(root, a, b):
    if root == None:
        return
    if root.val == a or root.val == b:
        return root.val

    left = commonAncestor(root.left, a, b)
    right = commonAncestor(root.right, a, b)

    if left == None:
        return right
    elif right == None:
        return left
    else:
        return root.val


root = Node(12)
root.left = Node(10)
root.right = Node(20)
root.right.left = Node(25)
root.right.right = Node(40)

print(commonAncestor(root, 10, 40))
