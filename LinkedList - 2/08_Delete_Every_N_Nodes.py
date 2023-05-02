from sys import stdin

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None



def skipMdeleteN(head, M, N):
    
    if M == 0 or head is None :
        return None

    if N == 0 :
        return head


    currentNode = head
    temp = None

    while currentNode is not None :
        take = 0
        skip = 0

        while currentNode is not None and take < M :
            if temp is None :
                temp = currentNode
            else :
                temp.next = currentNode
                temp = currentNode


            currentNode = currentNode.next
            take += 1


        while currentNode is not None and skip < N :
            currentNode = currentNode.next
            skip += 1


    if temp is not None :
        temp.next = None

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
    m_n = stdin.readline().strip().split(" ")

    m = int(m_n[0])
    n = int(m_n[1])

    newHead = skipMdeleteN(head, m, n)
    printLinkedList(newHead)

    t -= 1