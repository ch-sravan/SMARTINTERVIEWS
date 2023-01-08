def pairs(d,n,k):
    a=list(d.values())
    b=list(d.keys())
    c=0
    e=0
    for m in range(0,len(a)):
        t=k+b[m]
        if  t in d:
            c=1 
        else:
            e=1
    return c
t=int(input())
for i in range(t):
    n,k=map(int,input().strip().split())
    l=list(map(int,input().strip().split()))
    d={}
    for j in range(len(l)):
        if l[j] in d:
            d[l[j]]+=1
        else:
            d[l[j]]=1
    c=pairs(d,n,k)
    if(c==1):
        print("true")
    else:
        print("false")
