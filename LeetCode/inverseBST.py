class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def traverse(root):
    if root == None:
        return None
    traverse(root.left)
    print(root.val)
    traverse(root.right)

def inverseBST(root):
    if root == None:
        return None

    inverseBST(root.left)
    inverseBST(root.right)

    #inverse root

    temp = root.left
    root.left = root.right
    root.right = temp

    return root

root = TreeNode(10)
root.left = TreeNode(12)
root.right = TreeNode(15)
root.left.left  = TreeNode(25)
root.left.right  = TreeNode(30)
root.right.left  = TreeNode(36)

traverse(root)
print("\n\n")
inverseBST(root)
traverse(root)
