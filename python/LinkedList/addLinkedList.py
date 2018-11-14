class Node:
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
            temp = self.head
            while(temp):
                print(temp.data)
                temp = temp.next

def addTwoLists(first, second):
    firstNumber = ""
    head1 = first

    while head1:
        firstNumber = firstNumber + str(head1.data)
        head1 = head1.next

    secondNumber = ""
    head2 = first

    while head2:
        secondNumber = secondNumber + str(head2.data)
        head2 = head2.next

    firstNumber = int(firstNumber)
    secondNumber = int(secondNumber)
    final = firstNumber + secondNumber

    final = str(final)
    print(final)
    newHead = LinkedList()
    for i in range(len(final)):
        newHead.push(final[i])
    return newHead

# Driver program to test above function
first = LinkedList()
second = LinkedList()

# Create first list
first.push(6)
first.push(4)
first.push(9)
first.push(5)
first.push(7)
print("First List is ")
first.printList()

# Create second list
second.push(4)
second.push(8)
print("\nSecond List is ")
second.printList()

# Add the two lists and see result
print("\nResultant list is ")
res = addTwoLists(first.head, second.head)

res.printList()
