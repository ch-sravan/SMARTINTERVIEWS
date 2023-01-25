t=int(input())
for i in range(t):
    s=input()
    a=s.lower()
    b=list(a)
    v=0
    c=0
    w=len(s.split())
    for j in b:
        if(j=='a' or j=='e' or j=='i' or j=='o' or j=='u'):
            v+=1
        elif(j==' '):
            m=0
        else:
            c+=1
    print(w,v,c)
