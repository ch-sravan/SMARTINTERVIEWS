t=int(input())
for i in range(t):
    l=list(input())
    c=0
    a="."
    for j in range(len(l)):
        for k in range(j+1,len(l)):
            if(l[j]==l[k]):
                a=l[j]
                c=1
                break
        if(c==1):
            break
    print(a)
