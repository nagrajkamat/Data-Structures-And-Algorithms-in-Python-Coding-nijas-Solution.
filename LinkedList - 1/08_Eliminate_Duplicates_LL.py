from sys import stdin

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None




def removeDuplicates(head) :
    #Your code goes here
    if head is None or head.next is None:
        return head
    
    curr = head
    ntr = curr.next
    
    while ntr is not None:
        if curr.data == ntr.data:
            curr.next = ntr.next
            ntr= curr.next
        else:
            curr = curr.next
            ntr = ntr.next
            
    return head









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
t = int(stdin.readline().strip())

while t > 0 :
    head = takeInput()

    head = removeDuplicates(head)
    printLinkedList(head)

    t -= 1