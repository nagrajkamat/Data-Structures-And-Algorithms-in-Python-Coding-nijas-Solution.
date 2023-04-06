def mlp(n, m):
    if m==0:
        return 0
    elif m==1:
        return n
    elif m<0:
        return - (n - mlp(n, m+1))
    else:
        return n + mlp(n, m-1)
    
from sys import setrecursionlimit
setrecursionlimit(10**6)

m = int(input())
n = int(input())
print(mlp(n, m))