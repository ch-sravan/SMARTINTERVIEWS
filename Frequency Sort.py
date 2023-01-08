t=int(input())
for _ in range(t):
    n=int(input())
    a1=list(map(int,input().strip().split()))
    a=sorted(a1)
    l=[]
    dict1={}
    for i in range(len(a)):
        if a[i] in dict1:
             dict1[a[i]]+=1
        else:
             dict1[a[i]]=1
    a2= dict(sorted(dict1.items(), key=lambda item: item[1]))
    x=list(a2.values())
    y=list(a2.keys())
    for j in range(len(y)):
        if x[j]>0:
            for k in range(x[j]):
                l.append(y[j])
    for m in l:
        print(m,end=" ")
    print()
