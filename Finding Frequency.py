t=int(input())
l=list(map(int,input().strip().split()))
l1=sorted(l)
d={}
for i in range(t):
    if l1[i] in d:
        d[l1[i]]+=1
    else:
        d[l1[i]]=1
q=int(input())
for i in range(q):
    x=int(input())
    if x in d:
        print(d[x])
    else:
        print("0")
