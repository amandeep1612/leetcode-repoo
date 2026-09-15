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
        current=current.next
    return head

def printDLL(head):
    current=head
    while current:
        print(current.data,'-->')
        current=current.next
    print("None")

def deleteDLL(head):# deleting tail
    if head is None:
        return None
    current= head
    while current.next:
        current=current.next
        #current is now the tail 
    #disconnect the tail
    current.prev.next=None
    return head


    










values=[10,20,30,40]

head=createDLL(values)
print("DLL :-")
printDLL(head)
print("dll after deletion ")
deleteDLL(head)
printDLL(head)



