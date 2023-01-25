t=int(input())
for i in range(t):
    a,b=list(map(str,input().strip().split()))
    d={}
    c=[]
    for i in range(len(a)):
        if a[i] in d:
            d[a[i]]+=1
        else:
            d[a[i]]=1
    for i in range(len(b)):
        if b[i] not in d:
            c.append(b[i])
    s="".join(c)
    #print(c)
    print(s)
    
