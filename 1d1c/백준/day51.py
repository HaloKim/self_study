# 15649
from collections import deque

n,m = map(int, input().split())
q = deque()
visit = [0]*(n+1)
def dfs():
    if len(q) == m:
        print(*q)
        return

    for i in range(1, n+1):
        if visit[i] == 0:
            visit[i] = 1
            q.append(i)
            dfs()
            q.pop()
            visit[i] = 0
    return
dfs()