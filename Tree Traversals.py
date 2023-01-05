class Node:
    def __init__(this,data): 
        this.data = data 
        this.left = None  
        this.right = None 
def preorder(root):
    if(root==None):
        return
    print(root.data,end=" ")
    preorder(root.left)
    preorder(root.right)
def postorder(root):
    if(root==None):
        return
    postorder(root.left)
    postorder(root.right)
    print(root.data,end=" ")
def inorder(root):
    if(root==None):
        return
    
    inorder(root.left)
    print(root.data,end=" ")
    inorder(root.right)
def insert(root,a):
    if(root==None):
        n=Node(a)
        return n
    if(a<root.data):
        root.left=insert(root.left,a)
    else:
        root.right=insert(root.right,a)
    return root
t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().strip().split()))
    root=None
    for j in range(n):
        a=l[j]
        root=insert(root,a)
    preorder(root)
    print()
    inorder(root)
    print()
    postorder(root)
    print()
    print()
