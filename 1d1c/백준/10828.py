from collections import deque
from sys import stdin
input = stdin.readline

n = int(input())
arr = deque()
dis = deque()
for _ in range(n):
    a = input().strip()
    try:
        a,b = a.split()
    except:
        a = a
    if a == 'push':
        arr.append(b)
    if a == 'top':
        if not arr:
            dis.append(-1)
        else:
            dis.append(arr[-1])
    elif a == 'pop':
        if not arr:
            dis.append(-1)
        else:
            dis.append(arr.pop())
    elif a == 'size':
        dis.append(len(arr))
    elif a == 'empty':
        if arr:
            dis.append(0)
        else:
            dis.append(1)

print(*dis, sep='\n')