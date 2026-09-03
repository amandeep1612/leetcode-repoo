"""
head
 ↓
[10] -> [20] -> [30] -> None
         ↑
       current
"""
class ListNode:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def createLinkedList(values):
    if len(values) == 0:
        return None

    head = ListNode(values[0])
    current = head

    for i in range(1, len(values)):
        newNode = ListNode(values[i])
        current.next = newNode
        current = newNode

    return head


def insertAtHead(head, val):

    # Create new node
    newNode = ListNode(val)

    # Link new node to current head
    newNode.next = head

    # Make new node the new head
    head = newNode

    return head


def printLinkedList(head):
    current = head

    while current:
        print(current.data, end=" -> ")
        current = current.next

    print("None")


values = [10, 20, 30]

head = createLinkedList(values)

# Insert 5 at head
head = insertAtHead(head, 5)

printLinkedList(head)