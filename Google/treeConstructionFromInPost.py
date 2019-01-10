# construct tree from inorder and post order
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def func(inorder, postorder):
    print('func call ', inorder, postorder)
    if len(postorder) == 0:
        return None
    if len(postorder) == 1:
        return TreeNode(postorder.pop())

    root = TreeNode(postorder.pop())

    i = inorder.index(root.data)

    root.left = func(inorder[:i], postorder[:i])
    root.right = func(inorder[i+1:], postorder[i:])

    return root

def printTree(root):
    if root != None:
        print(root.data)
        printTree(root.left)
        printTree(root.right)

print(printTree(func([9,3,15,20,7],[9,15,7,20,3])))
