## Read input as specified in the question.
## Print output as specified in the question.
def printSubset(arr, k, lst):
    n=len(arr)
    if n==0:
        return
    if n==1:
        if arr[0]==k:
            print(k, *lst)
            return

    printSubset(arr[:-1], k, lst)
    printSubset(arr[:-1], k-arr[-1], [arr[-1]]+lst)
    if arr[-1]==k:
        print(k, *lst)

def printSubsetMain(arr, k):
    printSubset(arr, k, [])

n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
k=int(input())
printSubsetMain(arr, k)