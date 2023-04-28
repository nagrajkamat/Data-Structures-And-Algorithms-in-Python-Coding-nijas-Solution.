def checkMaxHeap(lst):
    n = len(lst)
    for i in range(n):
        left = (2*i) + 1
        right = left + 1
        if (left<n) and lst[left]>lst[i]:
            return False
        if (right<n) and lst[right]>lst[i]:
            return False
    return True

# Main Code
n=int(input())
lst=list(int(i) for i in input().strip().split(' '))
print('true') if checkMaxHeap(lst) else print('false')