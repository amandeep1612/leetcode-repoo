#CREATING A Linked List  

class ListNode:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
#create ll from list
def createLinkedList(values):
    if len(values)==0:
        return None
    #else create first node
    head=ListNode(values[0])
    current=head
    for i in range(1,len(values)):
        newNode=ListNode(values[i]) #creates new node
        current.next=newNode #links new and pre node 10->20->30->40
        current=newNode #moves current to new node
    return head 

def printLinkedList(head):
    current=head
    while current:
        print(current.data,end=" -> ")
        current=current.next
    print("None")




values=[10,20,30,40]
# Create linked list
head=createLinkedList(values)
# Print linked list
printLinkedList(head)