class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def getLinkedList(root):
    if root == None:
        return None, None

    lhead, ltail = getLinkedList(root.left)
    if lhead == None:
        lhead = root
    else:
        ltail.right = root
        root.left = ltail

    rhead, rtail = getLinkedList(root.right)
    if rhead == None:
        rtail = root
    else:
        rhead.left = root
        root.right = rhead

    return lhead, rtail


def bstToLinkedList(root):
    if root == None:
        return None

    head, tail = getLinkedList(root)

    while head!=None:
        print(head.val)
        head = head.right


root = TreeNode(10)
root.left = TreeNode(12)
root.right = TreeNode(15)
root.left.left  = TreeNode(25)
root.left.right  = TreeNode(30)
root.right.left  = TreeNode(36)

bstToLinkedList(root)
