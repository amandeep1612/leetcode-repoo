class ListNode:
    def __init__(self,data,next=None,prev=None):
        self.data=data
        self.next=None
        self.prev=None
def createDLL(values):
    if len(values)==0:
        return None
    head=ListNode(values[0])
    current=head
    for i in range(1,len(values)):
        newNode=ListNode(values[i])
        current.next=newNode
        newNode.prev=current
        current=newNode
    return head


def printForward(head):
    current=head
    while current:
        print(current.data,end=" -> " )
        current=current.next
    print("none")

def printBackward(head):
    if head is None:
        return None
    

    current=head
    while current.next:
        current=current.next #reach last node
    while current:
        print(current.data,end=" -> ")
        current=current.prev
    print("none")









values=[10,20,30]
head=createDLL(values)
print("forward :")
printForward(head)
print("backwards :")
printBackward(head)

