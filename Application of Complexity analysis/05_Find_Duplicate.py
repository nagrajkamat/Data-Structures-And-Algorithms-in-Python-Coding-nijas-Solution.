from sys import stdin


def findDuplicate(arr, n) :
    arr.sort()
    for i in range(len(arr)):
        if arr[i] ^ arr[i+1] ==0:
            return arr[i]
    #l=len(arr)
    #n=0
    #for i in range(0,l-1):
     #   n ^=i
      #  n ^=arr[i]
    #return n^arr[l-1]

#Taking input using fast I/O method
def takeInput() :
    n = int(stdin.readline().rstrip())

    if n == 0 :
        return list(), 0

    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    return arr, n


#main
t = int(stdin.readline().rstrip()) 

while t > 0 :

    arr, n = takeInput()
    print(findDuplicate(arr, n))

    t -= 1