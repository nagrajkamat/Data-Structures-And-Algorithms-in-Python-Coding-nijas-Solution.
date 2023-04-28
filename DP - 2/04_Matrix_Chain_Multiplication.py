import sys
from sys import stdin
def mcm(p,n):
	n+=1
	m=[[sys.maxsize for i in range (0,n+1)] for j in range (0,n+1)]
	for i in range (1,n):
		m[i][i]=0
	for l in range (2,n):
		for i in range (1,n-l+1):
			j=i+l-1
			for k in range (i,j):
				q=m[i][k]+m[k+1][j]+p[i-1]*p[k]*p[j]
				if(q<m[i][j]):
					m[i][j]=q
	return m[1][n-1]





n=int(stdin.readline().strip())
p=[int(i) for i in stdin.readline().strip().split()]
print(mcm(p,n))