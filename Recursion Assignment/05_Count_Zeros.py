import sys
sys.setrecursionlimit(10**6)
def countzero(n):
    if n%10 == 0:
        if n == 0:
            return 0
        return 1 + countzero(n//10)
    else:
        return countzero(n//10)
    
    

n = int(input())
if n == 0:
    print(1)
else:
	print(countzero(n))