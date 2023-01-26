n=int(input())
l=list(map(int,input().strip().split()))
ps=[]
r=0
for k in range(0,len(l)):
    r=r+l[k]
    ps.append(r)
t=int(input())
for i in range(t):
    a,b=map(int,input().strip().split())
    if(a>0):
        print(ps[b]-ps[a-1])
    else:
        print(ps[b])
