t=int(input())
for j in range(t):
    n=int(input())
    s=(input())
    l=list(s)
    r=0
    for i in range(0,len(l)):
        p1=i-1
        p2=i+1
        while(p1>=0 and p2<len(l) and l[p1]==l[p2]):
            p1-=1
            p2+=1
        r=max(r,p2-p1-1)
        p1=i
        p2=i+1
        while(p1>=0 and p2<len(l) and l[p1]==l[p2]):
            p1-=1
            p2+=1
        r=max(r,p2-p1-1)
    print(r)
