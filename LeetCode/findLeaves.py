# LeetCode xFind Leaves of Binary Tree (Java)
# Given a binary tree, collect a trees nodes as if you were doing this:
# Collect and remove all leaves, repeat until the tree is empty.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def findLeaves(root, res):
    if root == None:
        return True

    if root.left == None and root.right == None:
        res.append(root.val)
        return True

    if findLeaves(root.left, res) == True:
        root.left = None

    if findLeaves(root.right, res) == True:
        root.right = None

    return False

def main(root):
    res = []

    while findLeaves(root, res) != True:
        print(res)
        res = []
    print res


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(4)
main(root)
