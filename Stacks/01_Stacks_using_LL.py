from sys import stdin


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class Stack:
    def __init__(self):
        self.__head = None
        self.__cnt = 0
        
    def push(self, element):
        newNode = Node(element)
        newNode.next = self.__head
        self.__head = newNode
        self.__cnt += 1
        
        
    def pop(self):
        if self.isEmpty() is True:
            # print("Hey! Stack is Empty!!")
            return -1
        
        data = self.__head.data
        self.__head = self.__head.next
        self.__cnt -= 1
        
        return data
        
    def top(self):
        if self.isEmpty() is True:
            # print("Hey! Stack is Empty!!")
            return -1
        
        return self.__head.data
    
    def size(self):
        return self.__cnt
        
    def isEmpty(self):
        return self.size() == 0 
    
    
q = int(stdin.readline().strip())

stack = Stack()

while q > 0 :

    inputs = stdin.readline().strip().split(" ")
    choice = int(inputs[0])

    if choice == 1 :
        data = int(inputs[1])
        stack.push(data)

    elif choice == 2 :
        print(stack.pop())

    elif choice == 3 :
        print(stack.top())

    elif choice == 4 : 
        print(stack.size())

    else :
        if stack.isEmpty() :
            print("true")
        else :
            print("false")

    q -= 1

