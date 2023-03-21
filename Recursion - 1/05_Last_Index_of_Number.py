# Given an array of length N and an integer x, you need to find and return the last index of integer x present in the array. 
# Return -1 if it is not present in the array.
# Last index means - if x is present multiple times in the array, return the index at which x comes last in the array.
# You should start traversing your array from 0, not from (N - 1).
# Do this recursively. Indexing in the array starts from 0



def LastIndex(arr, x):
    l = len(arr)
    if l == 0:
        return -1
    
    SmallerList = arr[1:]
    
    SmallerListOutput = LastIndex(SmallerList, x)
    if SmallerListOutput != -1:
        return SmallerListOutput +1
    else:
        if arr[0] == x:
            return 0
        else:
            return -1

#main
from sys import setrecursionlimit
setrecursionlimit(11000)
n = int(input())
arr = list(int(i) for i in input().strip().split(' '))
x = int(input())
print(LastIndex(arr, x))

        
        
    
