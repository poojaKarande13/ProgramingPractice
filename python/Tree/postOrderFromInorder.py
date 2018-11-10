
# Python program to print postorder
# traversal from preorder and
# inorder traversals

def findPostOrderFromInorder(inorder, preorder, postorder):
    if len(preorder) < 0 or len(inorder) < 0:
        return
    root = 0
    if preorder[0] in inorder:
        root = inorder.index(preorder[0])

    if root != 0: # left tree exists
        findPostOrderFromInorder(inorder[:root], preorder[1:root+1], postorder)

    if root < len(inorder)-1: # left tree exists
        findPostOrderFromInorder(inorder[root+1:], preorder[root+1:], postorder)

    postorder.append(preorder[0])
    return

postorder = []
inorder = [4, 2, 5, 1, 3, 6];
preorder = [1, 2, 4, 5, 3, 6];

findPostOrderFromInorder(inorder, preorder, postorder)

print(postorder)
