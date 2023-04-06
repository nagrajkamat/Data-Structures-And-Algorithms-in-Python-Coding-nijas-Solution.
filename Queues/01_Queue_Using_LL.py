from sys import stdin

class Node :

    def __init__(self, data) :
        self.data = data
        self.next = None


class Queue :
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0


    '''----------------- Public Functions of Stack -----------------'''

    def getSize(self):
         return self.__size


    def isEmpty(self):
        return self.__size==0


    def enqueue(self,data):
        
        self.__size+=1
        newNode = Node(data)
        
        if self.__head is None:
            self.__head = newNode
            self.__tail=newNode
        else:
            self.__tail.next = newNode
            self.__tail = newNode     
        
        
    def dequeue(self):
        if self.isEmpty():
            return -1
        
        ans = self.__head.data
        self.__head = self.__head.next
        self.__size = self.__size - 1
        return ans

    def front(self):
        if self.isEmpty():
            return -1 
  
        return self.__head.data


#main
q = int(stdin.readline().strip())

queue = Queue()

while q > 0 :

    inputs = stdin.readline().strip().split(" ")
    choice = int(inputs[0])

    if choice == 1 :
        data = int(inputs[1])
        queue.enqueue(data)

    elif choice == 2 :
        print(queue.dequeue())

    elif choice == 3 :
        print(queue.front())

    elif choice == 4 : 
        print(queue.getSize())

    else :
        if queue.isEmpty() :
            print("true")
        else :
            print("false")

    q -= 1
