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
    
    
SOLUTION-2


for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().strip().split()))
    ans=0
    for i in range(n):
        ans^=l[i]
    for i in range(1,n-1):
        ans^=i
    for i in range(32):
        if((ans>>i)&1==1):
            pos=i
    a,b=0,0
    for i in range(n):
        if((l[i]>>pos)&1==1):
            a^=l[i]
        else:
            b^=l[i]
    for i in range(1,n-1):
        if((i>>pos)&1==1):
            a^=i
        else:
            b^=i
    print(*sorted([a,b]))
        
