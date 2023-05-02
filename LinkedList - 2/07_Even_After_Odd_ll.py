from sys import stdin

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None


def evenAfterOdd(head):
    if head is None:
        return head
    curr = head
    
    head1 = None
    head2 = None
    
    while curr is not None:
        if curr.data &1:
            if head1 is None:
                head1 = curr
                tail1 = curr
            else:
                tail1.next = curr
                tail1 = tail1.next
        else:
            if head2 is None:
                head2 = curr
                tail2 = curr
            else:
                tail2.next = curr
                tail2 = tail2.next
                        
        curr = curr.next
        
    if head1 is None or head2 is None:     
        return head
    
    tail2.next = None        
    tail1.next = head2
        
    return head1   




#Taking Input Using Fast I/O
def takeInput() :
    head = None
    tail = None

    datas = list(map(int, stdin.readline().rstrip().split(" ")))

    i = 0
    while (i < len(datas)) and (datas[i] != -1) :
        data = datas[i]
        newNode = Node(data)

        if head is None :
            head = newNode
            tail = newNode

        else :
            tail.next = newNode
            tail = newNode

        i += 1

    return head


#to print the linked list 
def printLinkedList(head) :

    while head is not None :
        print(head.data, end = " ")
        head = head.next

    print()


#main
t = int(stdin.readline().rstrip())

while t > 0 :
    
    head = takeInput()
    newHead = evenAfterOdd(head)
    printLinkedList(newHead)  
    
    t -= 1