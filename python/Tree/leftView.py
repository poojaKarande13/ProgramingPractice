# print left view of Binary Tree
class Node:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

# def traverseLevel(root, level, visited):
#     if root == None:
#         return
#
#     if visited[0] < level:
#         print(root.val)
#         visited[0] = level
#
#     traverseLevel(root.left, level+1, visited)
#     traverseLevel(root.right, level+1, visited)
#
# def leftView(root):
#     visited = [0]
#     traverseLevel(root, 1, visited)



root = Node(12)
root.left = Node(10)
root.right = Node(20)
root.right.left = Node(25)
root.right.right = Node(40)

leftView(root)
