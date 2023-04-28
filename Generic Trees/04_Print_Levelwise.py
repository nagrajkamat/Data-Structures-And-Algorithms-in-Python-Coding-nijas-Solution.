import sys
class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
    def __str__(self):
        return str(self.data)

import queue    
def printLevelWiseTree(tree):
    q = queue.Queue()
    if tree == None:
        return
    q.put(tree)
    
    while (not(q.empty())):
        current_node = q.get()
        print(current_node,':', ",".join(str(num) for num in current_node.children),
                sep='',end="")
        for child in current_node.children:
            q.put(child)
            # print(child.data, end="")
        print()
   

    
def takeTreeInputLevelWise():
    q = queue.Queue()
    print("Enter root")
    rootData = int(input())
    if rootData == -1:
        return None
    
    root = TreeNode(rootData)
    q.put(root)
    
    while (not(q.empty())):
        current_node = q.get()
        print("Enter number of childrens for ", current_node.data)
        numChildren = int(input())
        for i in range(numChildren):
            print("Enter next child for ", current_node.data)
            childData = int(input())
            child = TreeNode(childData)
            current_node.children.append(child)
            q.put(child)
            
    return root   
def createLevelWiseTree(arr):
    root = treeNode(int(arr[0]))
    q = [root]
    size = len(arr)
    i = 1
    while i<size:
        parent = q.pop(0)
        childCount = int(arr[i])
        i += 1
        for j in range(0,childCount):
            temp = treeNode(int(arr[i+j]))
            parent.children.append(temp)
            q.append(temp)
        i += childCount
    return root

# Main
sys.setrecursionlimit(10**6)
arr = list(int(x) for x in input().strip().split(' '))
tree = createLevelWiseTree(arr)
printLevelWiseTree(tree)