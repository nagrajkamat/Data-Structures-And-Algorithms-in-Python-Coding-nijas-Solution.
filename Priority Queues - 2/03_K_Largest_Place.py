import heapq as pq

def peekValue(heap) :
    peekValue = pq.heappop(heap)
    pq.heappush(heap, peekValue)
    
    return peekValue

def isEmpty(heap) :
    if len(heap) != 0 :
        return False
    
    return True

def kLargest(li, k) :
    heap = []
    for i in range(k) :
        pq.heappush(heap, li[i])
    
    
    for i in range(k, len(li)) :
        if li[i] > peekValue(heap) :
            pq.heappop(heap)
            pq.heappush(heap, li[i])
            
    ans = []
    
    while not isEmpty(heap) :
        ans.append(pq.heappop(heap))
        
    return ans
     
#main
n = int(input().strip())
arr = [int(elem) for elem in list(input().strip().split())]
k = int(input().strip())

ans = kLargest(arr, k)

for elem in ans :
	print(elem)
