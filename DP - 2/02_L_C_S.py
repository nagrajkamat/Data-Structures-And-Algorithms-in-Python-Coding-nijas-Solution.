
from sys import stdin

def lcs(s, t) :
    m = len(s)
    n = len(t)
    
    subProblems = [[0] * (n + 1) for i in range((m + 1))]


    for currStart in range(1, (m + 1)) :
        for currEnd in range(1, (n + 1)) :
            if s[m - currStart] == t[n - currEnd] :
                subProblems[currStart][currEnd] = 1 + subProblems[currStart - 1][currEnd - 1]
            else :
                subProblems[currStart][currEnd] = max(subProblems[currStart - 1][currEnd], subProblems[currStart][currEnd - 1])
                
    return subProblems[m][n]




s = str(stdin.readline().rstrip())
t = str(stdin.readline().rstrip())

print(lcs(s, t))