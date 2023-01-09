class Tree:
    def __init__(this,data):
        this.data=data
        this.right=None
        this.left=None
def insert(root,val):
    if(root==None):
        n=Tree(val)
        return n
    if(val<root.data):
        root.left=insert(root.left,val)
    else:
        root.right=insert(root.right,val)
    return root    
def h(root):
    if(root==None):
        return -1
    r=max(h(root.right),h(root.left))
    return r+1
t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().strip().split()))
    root=None
    for j in range(n):
        a=l[j]
        root=insert(root,a)
    print(h(root))
