t=int(input())
for i in range(t):
    s=list(input())
    l={}
    a="."
    for j in range(len(s)):
        if s[j] not in l:
            l[s[j]]=1
        else:
            a=s[j]
            break
    print(a)
    
