class ListNode:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
def createLinkedList(values):
    if len(values)==0:
        return None
    head=ListNode(values[0])
    current=head
    for i in range(1,len(values)):
        newNode=ListNode(values[i])
        current.next=newNode
        current=newNode
    return head

def deleteTail(head):
    #if ll is empty 
    if head is None:
        return None
    elif head.next is None:
        return None
    current=head
    #moves untill current reaches second last element
    while current.next.next is not None:
        current=current.next
    #remove last
    current.next=None
    return head
def printLinkedList(head):

    current = head

    while current:
        print(current.data, end=" -> ")
        current = current.next

    print("None")


values=[10,20,30]
head=createLinkedList(values)
print("Before deleting tail:")
printLinkedList(head)
# Delete last node
head = deleteTail(head)
print("After deleting tail:")
printLinkedList(head)