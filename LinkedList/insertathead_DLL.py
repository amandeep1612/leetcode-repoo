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
def insertAtHead(head,val):
    
    newNode=ListNode(val) #5
    newNode.next=head #5->head
    head.prev=newNode  #5->head(1)
    head=newNode #head=5 
    #none->5->1->2



def printForward(head):
    current=head
    while current:
        print(current.data,end=" -> " )
        current=current.next
    print("none")
    return head










values=[10,20,30]
head=createDLL(values)
print("list before insertion :")
printForward(head)
head=insertAtHead(head,5)
print("list after insertion :")
printForward(head)

print(head)
