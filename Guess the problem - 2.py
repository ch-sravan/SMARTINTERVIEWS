t=int(input())
for i in range(t):
    s,k=input().split(maxsplit=1)
    k=int(k)
    #print(k)
    l=[]
    for j in range(len(s)):
        b=ord(s[j])+k-97
        c=b%26
        print(chr(c+97),end="")
    print()
    
