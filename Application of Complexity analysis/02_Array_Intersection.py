from sys import stdin



def intersection(arr1, arr2, n, m) :
    arr1.sort()
    arr2.sort()
    m=len(arr1)
    n=len(arr2)
    i=0
    j=0
    while i<m and j<n:
        if arr1[i]<arr2[j]:
            i=i+1
        elif arr2[j]<arr1[i]:
            j=j+1
        else:
            print(arr2[j],end=' ')
            j=j+1
            i=i+1
    pass       
	#Your code g
# Taking input using fast I/O method
def takeInput() :
    n = int(stdin.readline().strip())
    
    if n == 0 :
    	return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


#main
t = int(stdin.readline().strip())

while t > 0 :

    arr1, n = takeInput()
    arr2, m = takeInput()
    intersection(arr1, arr2, n, m)
    print()

    t -= 1