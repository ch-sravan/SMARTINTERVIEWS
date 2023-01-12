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
            if l[k] in d:
                break
            d[l[k]]=1
            if(l[k]>=max1):
                max1=l[k]
            if(l[k]<=min1):
                min1=l[k]
            if(max1-min1==k-j):
                if(ans<=k-j+1):
                    ans=k-j+1
    print(ans)
                
