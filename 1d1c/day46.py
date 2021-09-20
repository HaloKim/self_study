import sys
from collections import deque

k = int(sys.stdin.readline())

def bfs(q):
    visit = [0]*(v+1)

    while q:
        x,y = q.popleft()

        if visit[x] == 0:
            visit[x] = 1
        else:
            visit[x] = visit[x]

        if visit[y] == 0:
            visit[y] = visit[x]*(-1)
        else:
            visit[y] = visit[y]

        if visit[x] == visit[y]:
            return 0
    return 1

for _ in range(k):
    v,e = map(int, sys.stdin.readline().strip().split())
    q = deque()
    q2 = deque()
    for i in range(e):
        a,b = map(int, sys.stdin.readline().strip().split())
        q.append([a,b])
        q2.append([b,a])
    if bfs(q)+bfs(q2) >= 1:
        print("YES")
    else:
        print("NO")