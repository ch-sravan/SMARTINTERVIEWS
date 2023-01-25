t=int(input())
for i in range(t):
    n,k=map(int,input().strip().split())
    l=list(map(int,input().strip().split()))
    d={}
    for j in range(k):
        if l[j] in d:
            d[l[j]]+=1
        else:
            d[l[j]]=1
    print(len(d),end=" ")
    for m in range(k,n):
        d[l[m-k]]-=1
        if d[l[m-k]]==0:
            d.pop(l[m-k])
        if l[m] in d:
            d[l[m]]+=1
        else:
            d[l[m]]=1
        print(len(d),end=" ")
    print()
        
