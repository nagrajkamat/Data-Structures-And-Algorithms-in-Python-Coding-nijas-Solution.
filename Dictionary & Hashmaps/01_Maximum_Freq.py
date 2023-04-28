from sys import stdin
def maxfreq(arr):
    d = {} 
    for num in arr: 
        if num in d: 
            d[num] += 1 
        else: 
            d[num] = 1 
    ans = arr[0] 
    for num in arr: 
        if d[num] > d[ans]: 
            ans = num 
    return ans 

    
    
    
    
def takeInput():
    #To take fast I/O
    n=int(stdin.readline().strip())
    if n==0:
        return list(),0
    arr=list(map(int,stdin.readline().strip().split( )))
    return arr,n

arr,n=takeInput()
print(maxfreq(arr))