t=int(input())
for i in range(t):
    a,b=map(int,input().strip().split())
    c=0
    l1=[]
    for j in range(a):
        l=list(input())
        d=sorted(l)
        e="".join(d)
        l1.append(e)
    #print(l1)
    t=set(l1)
    print(len(t))
    
