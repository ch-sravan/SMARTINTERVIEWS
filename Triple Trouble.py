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

            
SOLUTION-2


for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().strip().split()))
    ans=0
    for b in range(32):
        c=0
        for i in range(n):
            if ((l[i]>>b)&1)==1:
                c+=1
        if(c%3!=0):
            ans+=1<<b
    print(ans)
            
