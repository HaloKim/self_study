import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

N = int(input())
M = int(input())
visit = [INF]*(N+1)
bus = [[] for _ in range(N+1)]
for i in range(M):
    a,b,c = map(int, input().strip().split())
    bus[a].append([b,c])
start, end = map(int, input().split())
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    visit[start] = 0
    while q:
        w, vertex = heapq.heappop(q)
        if visit[vertex] < w:
            continue
        for v, bcost  in bus[vertex]:
            cost = w + bcost
            if cost < visit[v]:
                visit[v] = cost
                heapq.heappush(q, (cost, v))
    return
dijkstra(start)
print(visit[end])