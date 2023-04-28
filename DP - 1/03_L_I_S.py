from sys import stdin
def lis(arr): 
    storage = [None for i in range(n)]
    storage[0] = 1

    ans = 1

    for i in range(1 , n):
        max = 1
        for j in range(i - 1 , -1 , -1):
            if (arr[j] < arr[i]):
                op = storage[j] + 1

                if (op > max):
                    max = op          
        

        storage[i] = max

        if (max > ans):
            ans = max
    
    return ans

       

def takeInput():
    #To take fast I/O
    n=int(stdin.readline().strip())
    if n==0:
        return list(),0
    arr=list(map(int,stdin.readline().strip().split( )))
    return arr,n
    

arr,n=takeInput()
print(lis(arr))