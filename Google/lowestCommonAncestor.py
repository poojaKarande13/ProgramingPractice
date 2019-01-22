class TreeNode:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

def ifPresent(root, val1):
    res1 = False
    if root.val == val1:
        res1 = True

    if root.left != None:
        res1 |= ifPresent(root.left, val1)

    if root.right != None:
        res1 |= ifPresent(root.right, val1)

    return res1

def findAncestor(root, val1, val2):
    if root == None:
        return False
    if root.val == val1:
        return val1

    if root.val == val2:
        return val2

    left = findAncestor(root.left, val1, val2)

    right = findAncestor(root.right, val1, val2)

    if left != False and right != False:
        return root.val
    if left == False:
        return right
    if right == False:
        return left


def main(root, val1, val2):
    if root == None:
        return None

    res1 = ifPresent(root, val1)
    res2 = ifPresent(root, val2)

    if res1 == False or res2 == False:
        return -1

    return findAncestor(root, val1, val2)

root = TreeNode(3)
root.left = TreeNode(5)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)

root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)

root.right = TreeNode(1)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)

print(main(root, 5, 4))
