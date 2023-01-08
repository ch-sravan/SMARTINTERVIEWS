t=int(input())
for i in range(t):
    n=int(input())
    a=bin(n)
    b=list(a[2:])
    if(len(b)%2!=0):
        b.insert(0,'0')
    i=0
    while(i<len(b)):
        temp=b[i]
        b[i]=b[i+1]
        b[i+1]=temp 
        i+=2
    c='0'
    for j in range(len(b)):
        c+=b[j]
    r=int(c,2)
    print(r)
    
