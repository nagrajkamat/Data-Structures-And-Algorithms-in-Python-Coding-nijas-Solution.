# Write your code here
from sys import stdin, setrecursionlimit
setrecursionlimit(10**6)
import queue
class Graph:
    def __init__(self, nVertices):
        self.nVertices = nVertices
        self.adjMatrix = [[0 for i in range(nVertices)] for j in range(nVertices)]
    
    def addEdge(self, v1, v2):
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1
    
    def removeEdge(self):
        if self.containsEdge(v1, v2) is False :
            return
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v1] = 0
        
    def containsEdge(self, v1, v2):
        if self.adjMatrix[v1][v2] > 0:
            return True
        else: 
            return False
        
    def __str__(self):
        return str(self.adjMatrix)
            
    
    def __getPathBFS(self, sv, ev, visited) :
        mapp = {}
        q = queue.Queue()
        
        if self.adjMatrix[sv][ev] == 1 and sv == ev :
            ans = []
            ans.append(sv)
            return ans
        
        q.put(sv)
        visited[sv] = True
        
        while q.empty() is False :
            front = q.get()
            
            for i in range(self.nVertices) :
                if self.adjMatrix[front][i] == 1 and visited[i] is False :
                    mapp[i] = front
                    q.put(i)
                    
                    visited[i] = True
                    
                    if i == ev :
                        ans = []
                        ans.append(ev)
                        value = mapp[ev]
                        
                        while value != sv :
                            ans.append(value)
                            value = mapp[value]
                        
                        ans.append(value)
                        return ans
    
        return []
        
        
    def getPathBFS(self, sv, ev) :
        
        # Return empty list in case sv or ev is invalid
        if (sv > (self.nVertices - 1)) or (ev > (self.nVertices - 1)) :
            return list()
        visited = [False for i in range(self.nVertices)]
        return self.__getPathBFS(sv, ev, visited)
        

# Main
li = stdin.readline().strip().split()
V = int(li[0])
E = int(li[1])

g = Graph(V)

for i in range(E) :
    arr = stdin.readline().strip().split()
    fv = int(arr[0])
    sv = int(arr[1])
    g.addEdge(fv, sv)

li = stdin.readline().strip().split()
sv = int(li[0])
ev = int(li[1])

li = g.getPathBFS(sv, ev)

if len(li) != 0 :
	for element in li :
		print(element, end = ' ')