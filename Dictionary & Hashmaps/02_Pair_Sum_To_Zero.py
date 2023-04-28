from sys import stdin
from math import factorial

def nc2(n):
    ans=0
    if n!=1:
        ans = factorial(n) / (factorial(2)*factorial(n-2))
    return int(ans)

def freqMap(l):
    map={}
    for num in l:
        if num in map:
            map[num]+=1
        else:
            map[num]=1
    return map


def pairSum0(l,n):
    m=freqMap(l)
    count = 0
    for num in m:
        if num>0 and -num in m:
            count = count + (m[num]*m[-num])
                
        if num==0:
            count = count + nc2(m[num])
    return count       


                




    
def takeInput():
    #To take fast I/O
    n=int(stdin.readline().strip())
    if n==0:
        return list(),0
    arr=list(map(int,stdin.readline().strip().split( )))
    return arr,n

arr,n=takeInput()
print(pairSum0(arr,n))