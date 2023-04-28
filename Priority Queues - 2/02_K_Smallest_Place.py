import heapq
def kSmallest(lst, k):
    maxHeap = []
    heapq.heapify(maxHeap) 
    n = len(lst)
    for i in range(0,k):
        heapq.heappush(maxHeap,-1*lst[i])# Add first k elements to max heap by negating elements
    for i in range(k,n):
        if -1*lst[i]>maxHeap[0]:
            heapq.heappop(maxHeap)
            heapq.heappush(maxHeap, -1*lst[i])
    multiplied_list = [element * -1 for element in maxHeap]
    return multiplied_list


# Main
n=int(input())
lst=list(int(i) for i in input().strip().split(' '))
k=int(input())
ans=kSmallest(lst, k)
ans.sort()
print(*ans, sep=' ')