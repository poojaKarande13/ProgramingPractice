# https://leetcode.com/problems/print-binary-tree/
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def getHeight(self,root):
        if root == None:
            return 0
        return (1 + max(self.getHeight(root.left) + self.getHeight(root.right))

    def printTree(self, root):
        rows = self.getHeight(root)
        cols = pow(2, rows) - 1
        print(rows, cols)

        res = [["" for i in range(cols)] for j in range(rows)]
        self.fillMatrix(res, root, 0,0, cols)

        return res

    def fillMatrix(self, mat, root, i,  l, h):
        if root != None:
            mid = (l + h) / 2
            #print("new ",mat, i, l, h, mid, root.val)
            mat[i][mid] = root.val
            self.fillMatrix(mat, root.left, i+1, l, (l + h) / 2)
            self.fillMatrix(mat, root.right, i+1, (l+h+1)/2, h)
        return mat

obj = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(4)
mat = obj.printTree(root)

print(mat)
