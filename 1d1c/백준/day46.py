# 1707
import sys
from collections import deque

k = int(sys.stdin.readline())
    
for _ in range(k):
    v,e = map(int, sys.stdin.readline().strip().split())
    graph = [[] for _ in range(v+1)]
    visit = [0]*(v+1)
    for i in range(e):
        a,b = map(int, sys.stdin.readline().strip().split())
        graph[a].append(b)
        graph[b].append(a)
    flag = 1
    q = deque()
    for i in range(1,v+1):
        if visit[i] == 0:
            q.append(i)
            visit[i] = 1
            while q:
                dot = q.popleft()
                for j in graph[dot]:
                    if visit[j] == 0:
                        q.append(j)
                        visit[j] = -1 * visit[dot]
                    elif visit[j] == visit[dot]:
                        flag = 0
    if flag == 0:
        print('NO')
    else:
        print('YES')