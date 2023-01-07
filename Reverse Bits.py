t=int(input())
for i in range(t):
    n=int(input())
    a='{:032b}'.format(n)
    b=a[::-1]
    r=int(b,2)
    print(r)
