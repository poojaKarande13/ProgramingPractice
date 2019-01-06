# You have a binary search tree and integer n,
# find out the most efficient way to locate two nodes of the tree whose summation is equaled to "n" ?
# # 11
#           5
#         /    \
#     2          8
#   /         /     \
# 1       4   6       10
#     3           7 9

def searchBST(head, n):
    if head == None:
        return False
    elif head.val == n:
        return True
    elif head.val > n:
        return searchBST(head.left, n)
    elif head.val < n:
        return searchBST(head.right, n)

# assuming all numbers are positive
def findNodeBSTWithSum(head, n):
    if head == None:
        return -1
    if n == 0:
        return -1

    if n < head.val:
        return findNodeBSTWithSum(head.left, n)
    else:
        # search if head and n-head are the 2 nodes
        t = n - head.val
        if t > head.val
            res = search(head.right,t)
        else
            res = search(head.left,t)
        if res == True:
            return (head.val, t)

        res = findNodeBSTWithSum(head.left, n)
        if res != -1:
            return res

        res = findNodeBSTWithSum(head.right, n)
        if res != -1:
            return res
