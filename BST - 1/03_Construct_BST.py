import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def constructBST(lst):
    n=len(lst)
    if lst==None or n<=0:
        return None
    rootIndex = (n-1)//2
    root = BinaryTreeNode(lst[rootIndex])
    root.left = constructBST(lst[:rootIndex])
    root.right = constructBST(lst[rootIndex+1:])
    return root
    
    

def preOrder(root):
    # Given a binary tree, print the preorder traversal of given tree. Pre-order
    # traversal is: Root LeftChild RightChild
    if root==None:
        return
    print(root.data, end=' ')
    preOrder(root.left)
    preOrder(root.right)

# Main
n=int(input())
if(n>0):
    lst=[int(i) for i in input().strip().split()]
else:
    lst=[]
root=constructBST(lst)
preOrder(root)