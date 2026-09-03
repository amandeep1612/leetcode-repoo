# -----------------------------
# Node class
# -----------------------------
class ListNode:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


# -----------------------------
# Create Linked List
# -----------------------------
def createLinkedList(values):

    # Empty list
    if len(values) == 0:
        return None

    # Create first node
    head = ListNode(values[0])

    # current points to the last created node
    current = head

    # Create remaining nodes
    for i in range(1, len(values)):

        # Create a new node
        newNode = ListNode(values[i])

        # Connect current node to new node
        current.next = newNode

        # Move current to the new node
        current = newNode

    return head


# -----------------------------
# Search Element
# -----------------------------
def searchElement(head, key):

    # Start from first node
    current = head

    # Traverse linked list
    while current:

        # Check current node
        if current.data == key:
            return True

        # Move to next node
        current = current.next

    # Key not found
    return False


# -----------------------------
# Print Linked List
# -----------------------------
def printLinkedList(head):

    current = head

    while current:
        print(current.data, end=" -> ")
        current = current.next

    print("None")


# -----------------------------
# Main
# -----------------------------

values = [10, 20, 30]

# Create linked list
head = createLinkedList(values)

# Print linked list
printLinkedList(head)

# Search for element
key = 30

if searchElement(head, key):
    print("Element found")
else:
    print("Element not found")
    