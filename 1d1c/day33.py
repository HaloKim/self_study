# 1202 시간초과때문에 어려웠다.
import sys
import heapq
n,k = map(int, sys.stdin.readline().split())

jewel = []
for _ in range(n):
    w,v = map(int, sys.stdin.readline().split())
    heapq.heappush(jewel, [w,v])

bag = []
for _ in range(k):
    heapq.heappush(bag, int(sys.stdin.readline()))

total = 0
tmp = []
for _ in range(k):
    capacity = heapq.heappop(bag)
    while jewel and capacity >= jewel[0][0]:
        [w,v] = heapq.heappop(jewel)
        heapq.heappush(tmp, -v)
    if tmp:
        total -= heapq.heappop(tmp)
    elif not bag:
        break
print(total)
'''
3 3
3 200
5 500
3 100
1
5
3
'''