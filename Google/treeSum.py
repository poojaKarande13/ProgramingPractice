class TreeNode:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

def calculateRootToLeaf(root, sum):
    if root == None:
        return 0

    if root.left == None and root.right == None:
        # root is leaf node
        return sum * 10 + root.val

        leftSum = calculateRootToLeaf(root.left, sum * 10 + root.val)
        rightSum = calculateRootToLeaft(root.right, sum *10 + root.val)

        return leftSum + rightSum

def main(root):
    sum = 0
    if root == None:
        return 0

    leftSum = calculateRootToLeaf(root.left, sum * 10 + root.val)
    rightSum = calculateRootToLeaf(root.right, sum *10 + root.val)

    sum = leftSum + rightSum
    return (sum % 1003)


root = TreeNode(1)
root.left = TreeNode(2)
# root.left.left = TreeNode(6)
# root.left.right = TreeNode(2)

# root.left.right.left = TreeNode(7)
# root.left.right.right = TreeNode(4)

root.right = TreeNode(3)
# root.right.left = TreeNode(0)
# root.right.right = TreeNode(8)

print(main(root))
