# Write a function to see if a binary tree ↴ is "superbalanced"
# A tree is "superbalanced" if the difference between the depths of any two leaf nodes ↴ is no greater than one.

class Node(object):
  def __init__(self, value):
      self.value = value
      self.left  = None
      self.right = None

def balancedBinaryTree(root):
    if root == None:
        return 0

    lheight = balancedBinaryTree(root.left)
    rheight = balancedBinaryTree(root.right)

    if lheight != rheight or lheight == -1 or rheight == -1:
        return -1
    else:
        return lheight + 1

root = Node(12)
root.left = Node(10)
root.left.right = Node(3)
root.left.left = Node(3)
root.right = Node(20)
root.right.left = Node(25)
root.right.right = Node(40)

print(balancedBinaryTree(root))
