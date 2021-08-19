# 1463
''' 시간초과 ..
n = int(input())
count = 0
def temp(n):
    global count
    arr = [n]
    if (n-1) % 3 == 0:
        count += 1
        arr[0] = n-1
    if arr[0]%3 == 0 and arr[0] >= 3:
        count += 1
        arr.append(arr[0]//3)
    elif arr[0]%2 == 0 and arr[0] >= 2:
        count += 1
        arr.append(arr[0]//2)
    # print(arr)
    return arr
while(True):
    if n == 1:
        print(count)
        break
    tmp = temp(n)
    n = min(tmp)
'''

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