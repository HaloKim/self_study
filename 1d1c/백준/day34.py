# 5585
'''
import sys
n = int(sys.stdin.readline())

n = 1000 - n
coin = [500,100,50,10,5,1]

cnt = 0
while n:
    for i in coin:
        if i <= n:
            n -= i
            cnt += 1
            break
print(cnt)
'''

# 10162
'''
import sys
time = [300,60,10]
n = int(sys.stdin.readline())
if n%10 > 0:
    print(-1)
else:
    arr = [0,0,0]
    while(n):
        for i in range(len(time)):
            if n >= time[i]:
                n -= time[i]
                arr[i] += 1
                break
    print(*arr)
'''

# 2217 시간초과 더쉬운방법이있었다..
'''
import sys
n = int(sys.stdin.readline())
rope = [0]*n
for i in range(n):
    rope[i] = int(sys.stdin.readline())
rope.sort(reverse=True)
total = 0
for i in range(n):
    if rope[i]*(i+1) > total:
        total = rope[i]*(i+1)
print(total)
'''
'''
3
10
10
6
-
5
3
5
10
8
5
'''
# 1946 시간초과 ..
import sys
n = int(sys.stdin.readline())

for i in range(n):
    tmp = int(sys.stdin.readline())
    arr = []
    for j in range(tmp):
        a,b = map(int,sys.stdin.readline().split())
        arr.append([a,b])
    arr.sort()
    cnt = 1
    compare = arr[0][1]
    for j in range(1,tmp):
        if arr[j][1] < compare:
            cnt += 1
            compare = arr[j][1]
    print(cnt)