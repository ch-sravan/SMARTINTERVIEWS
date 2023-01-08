def XOR(a,n):
    xor=0
    for i in range(0,n):
        xor=xor^a[i]
    return xor*2
t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().strip().split()))
    print(XOR(a,n))
