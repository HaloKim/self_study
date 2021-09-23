# 1715
import sys
import heapq

n = int(sys.stdin.readline())
card = []

for i in range(n):
    heapq.heappush(card, int(sys.stdin.readline()))

if len(card) == 1:
    print(0)
else:
    ans = 0
    while len(card) > 1:
        temp1 = heapq.heappop(card)
        temp2 = heapq.heappop(card)
        ans += temp1 + temp2
        heapq.heappush(card, temp1 + temp2)
    print(ans)