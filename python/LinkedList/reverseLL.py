# Reverse Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse(head):
    prv = None
    curr = head
    nxt = None

    while curr:
        nxt = curr.next
        curr.next = prv
        prv = curr
        curr = nxt

    return prv

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(5)

head = reverse(head)
while head:
    print(head.data)
    head = head.next
