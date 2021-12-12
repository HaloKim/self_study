from collections import deque

def solution(n, edge):
    arr = [[] for _ in range(n+1)]
    for s,e in edge:
        arr[s].append(e)
        arr[e].append(s)
    visit = [0]*(n+1)
    bfs(arr,visit,1)
    return visit.count(max(visit))

def bfs(arr,visit,start):
    q = deque()
    q.append(start)
    visit[start] = 1
    while q:
        start = q.popleft()
        for i in arr[start]:
            if visit[i] == 0:
                visit[i] = visit[start]+1
                q.append(i)