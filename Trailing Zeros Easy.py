t=int(input())
for i in range(t):
    n=int(input())
    if(n<0):
        print("0")
    count=0
    while(n>=5):
        n//=5
        count+=n
    print(count)
        
