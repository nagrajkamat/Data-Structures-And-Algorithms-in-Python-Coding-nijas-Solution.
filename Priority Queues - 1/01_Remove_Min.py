class PriorityQueueNode:
    def __init__(self,ele,priority):
        self.ele = ele
        self.priority = priority
        
class PriorityQueue:
    def __init__(self):
        self.pq = []
    
    def isEmpty(self):
        return self.getSize() == 0
    
    def getSize(self):
        return len(self.pq)

    def getMin(self):
        if self.isEmpty():
            return None
        return self.pq[0].ele
    
    def __percolateUp(self):
        childIndex = self.getSize() - 1
        while childIndex > 0:
            parentIndex = (childIndex-1)//2
            
            if self.pq[parentIndex].priority > self.pq[childIndex].priority:
                self.pq[parentIndex],self.pq[childIndex] = self.pq[childIndex],self.pq[parentIndex]
                childIndex = parentIndex
            else:
                break
    def __percolateDown(self):
        parentIndex = 0
        leftIndex = 2*parentIndex + 1
        rightIndex = 2*parentIndex + 2
        while leftIndex < self.getSize():
            minIndex = parentIndex
            if(self.pq[minIndex].priority > self.pq[leftIndex].priority):
                minIndex = leftIndex
            if(rightIndex < self.getSize() and self.pq[minIndex].priority > self.pq[rightIndex].priority):
                minIndex = rightIndex
            
            if minIndex!=parentIndex:
                self.pq[parentIndex],self.pq[minIndex] = self.pq[minIndex],self.pq[parentIndex]
                parentIndex = minIndex
                leftIndex = 2*parentIndex + 1
                rightIndex = 2*parentIndex + 2
            else:
                break
            
    