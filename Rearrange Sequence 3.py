t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().strip().split()))
    ans=0
    for j in range(len(l)):
        d={}
        max1=-2147483648
        min1=2147483647
        for k in range(j,len(l)):
            d[l[k]]=1
            max1=max(l[k],max1)
            min1=min(l[k],min1)
            if(max1-min1+1==len(d)):
                if(ans<=k-j+1):
                    ans=max(ans,k-j+1)
    print(ans)
