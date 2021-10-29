import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def dfs(start,before):
    if visit[start] == 1: 
        return start

    visit[start] = 1

    for i in station[start]:
        if i == before: 
            continue  # 양방향 그래프기 때문
        result = dfs(i,start)
        if result >= 0:
            visit[start] = 2
            return result if start != result else -1

    return -1


def bfs():
    q = []
    for i in range(n):
        if visit[i] == 2: 
            q.append(i)
            dist[i] = 0

    while q:
        tmp = []

        for start in q:
            for nv in station[start]:
                if dist[nv] != -1: continue
                dist[nv] = dist[start] + 1
                tmp.append(nv)

        q = tmp



n = int(input())
station = [[] for _ in range(n)]
visit = [0]*n
dist = [-1]*n

for _ in range(n):
    a,b = map(int, input().split())
    station[a-1].append(b-1)
    station[b-1].append(a-1)

dfs(0,-1)
print(visit)
bfs()
print(*dist)