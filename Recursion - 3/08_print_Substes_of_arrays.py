## Read input as specified in the question.
## Print output as specified in the question.
def printsubsetHelper(arr, lst):
    n=len(arr)
    if(n==0):
        for number in lst:
            print(number, end=' ')
        print()
        return

    printsubsetHelper(arr[1:], lst)
    newLst = lst.copy()
    newLst.append(arr[0])
    printsubsetHelper(arr[1:], newLst)
    return

def printsubset(arr):
    printsubsetHelper(arr,[])

n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
printsubset(arr)