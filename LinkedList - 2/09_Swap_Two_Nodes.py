from sys import stdin

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None



def swapNodes(head, i, j):
    ptr1 = head
    ptr2 = head
    
    cnt1 = 0
    cnt2 = 0
    
    while cnt1 < i:
        cnt1 += 1
        ptr1 = ptr1.next
        
    while cnt2 < j:
        cnt2 += 1
        ptr2 = ptr2.next
        
    curr1 = ptr1
    curr2 = ptr2
    
    data1 = curr1.data
    data2 = curr2.data

    curr1.data = data2
    curr2.data = data1

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




def printLinkedList(head) :

    while head is not None :
        print(head.data, end = " ")
        head = head.next

    print()


#main
t = int(stdin.readline().rstrip())

while t > 0 :
    
    head = takeInput()
    i_j = stdin.readline().strip().split(" ")

    i = int(i_j[0])
    j = int(i_j[1])

    newHead = swapNodes(head, i, j)
    printLinkedList(newHead)

    t -= 1