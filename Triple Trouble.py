t=int(input())
for i in range(t):
    n=int(input())
    l1=list(map(int,input().strip().split()))
    l=sorted(l1)
    d={}
    for j in range(n):
        if l[j] not in d:
            d[l[j]]=1
        else:
            d[l[j]]+=1
    a=list(d.values())
    b=list(d.keys())
    for i in range(len(a)):
        if(a[i]==1):
            print(b[i])
