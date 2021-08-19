def calc(l):
    global ans
    ans+=1
    nl=[]
    for a in l:
        nl.append(a-1)
        if a%3==0 and a>=3:
            nl.append(a/3)
        if a%2==0 and a>=2:
            nl.append(a/2)
        print(nl)
    return nl

n=int(input())
l=[]
l.append(n)
ans=0
while(1):
    if min(l)==1:
        break
    l=calc(l)
print(ans)