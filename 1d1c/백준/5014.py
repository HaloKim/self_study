from collections import deque

F, S, G, U, D = map(int, input().split())
D = -D
visit = [0]*(F+1)
def bfs(S):
    q = deque()
    q.append(S)
    visit[S] = 1
    while q:
        v = q.popleft()
        if v == G:
            return visit[v]-1
        for i in U,D:
            dv = v + i
            if 1 <= dv <= F:
                if visit[dv] == 0:
                    visit[dv] = visit[v] + 1
                    q.append(dv)
    return 'use the stairs'
print(bfs(S))