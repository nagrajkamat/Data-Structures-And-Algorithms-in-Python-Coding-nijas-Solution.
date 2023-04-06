def findstep(n):
    if n==0:
        return 1
    elif n < 0:
        return 0
    else:
        return findstep(n-3) + findstep(n-2) + findstep(n-1)
    
n = int(input())
print(findstep(n))