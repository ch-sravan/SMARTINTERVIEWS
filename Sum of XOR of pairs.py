for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().strip().split()))
    s=0
    for j in range(31):
        c=0
        for k in range(n):
            if((l[k]>>j)&1==1):
                c+=1
        r=c*(n-c)
        s+=r*(1<<j)
    print(2*s)
        
