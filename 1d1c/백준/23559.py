import heapq
from sys import stdin
input = stdin.readline

N,K = map(int,input().strip().split())
heapa = []
ans = 0
for i in range(N):
    a,b = map(int, input().strip().split())
    heapq.heappush(heapa, [-abs(a-b), a,b])
for i in range(N):
    _, a,b = heapq.heappop(heapa)
    if a > b and K - 5000 >= 1000*(N-i-1):
        K -= 5000
        ans += a
    else:
        K -= 1000
        ans += b
print(ans)