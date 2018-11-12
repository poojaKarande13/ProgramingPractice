"""Return reference of new head of the reverse linked list
  The input list will have at least one element
  Node is defined as
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reversePart(head, k):
    prv = None
    curr = head
    nxt = None

    count = 0
    while curr and count < k:
        nxt = curr.next
        curr.next = prv
        prv = curr
        curr = nxt
        count += 1

    head.next = curr
    return prv, head

def reverse(head, k):
    prv = None
    curr = head
    newHead = None

    while curr:
        h, t  = reversePart(curr, k)
        if newHead == None:
            newHead = h
            curr = t.next
            prv = t
        else:
            prv.next = h
            prv = t
            curr = t.next
    return newHead

#5 9 9 3 5 6 6 2 8 2
#2
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)
head.next.next.next.next.next.next = Node(7)
head = reverse(head, 2)

while head:
    print(head.data)
    head = head.next
