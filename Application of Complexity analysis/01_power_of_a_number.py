def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n-1)
    return 

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
x, n=list(int(i) for i in input().strip().split(' '))
print(power(x, n))
