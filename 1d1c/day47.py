# 11724
import sys
from collections import deque

n,m = map(int, sys.stdin.readline().strip().split())
graph = [[] for _ in range(n+1)]
visit = [0 for _ in range(0,n+1)]

for _ in range(m):
    a,b = map(int, sys.stdin.readline().strip().split())
    graph[a].append(b)
    graph[b].append(a)

q = deque()
cnt = 0
for i in range(1,n+1):
    if visit[i] == 0:
        cnt += 1
        q.append(i)
        visit[i] = cnt
        while q:
            v = q.popleft()
            for w in graph[v]:
                if visit[w] == 0:
                    visit[w] = cnt
                    q.append(w)
print(max(visit))