t=int(input())
for i in range(t):
    n=int(input())
    l1=list(map(int,input().strip().split()))
    d={}
    l=sorted(l1)
    for j in range(len(l)):
        if l[j] in d:
            d[l[j]]+=1
        else:
            d[l[j]]=1
    a=list(d.values())
    b=list(d.keys())
    for k in range(len(a)):
        if(a[k]>1):
            print(b[k],end=" ")
    print()
