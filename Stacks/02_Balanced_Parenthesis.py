
from sys import stdin


def isBalanced(string):
    s = []
    for char in string:
        if char in '({[':
            s.append(char)
        elif char is ')':
            if(not s or s[-1]!='('):
                return False
            s.pop()
            
        elif char is '}':
            if(not s or s[-1]!='{'):
                return False
            s.pop()
        elif char is ']':
            if(not s or s[-1]!='['):
                return False
            s.pop()
    if(not s):
        return True
    return False
            

#main
string = stdin.readline().strip()

if isBalanced(string) :
	print("true")

else :
	print("false")
