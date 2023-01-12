t=int(input())
for i in range(t):
    x=int(input())
    if(x<0):
        x=abs(x)
        print(round(x**(1/3))*-1)
    else:
        print(round(x**(1/3)))
