N, M = map(int, input().split())
arr = [[] for _ in range(N)]
visit = [0]*N

for i in range(M):
    a,b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

def dfs(idx, cnt):
    if cnt >= 4:
        print(1)
        exit()
    for i in arr[idx]:
        if not visit[i]:
            visit[i] = 1
            dfs(i, cnt+1)
            visit[i] = 0

for i in range(N):
    visit[i] = 1
    dfs(i, 0)
    visit[i] = 0
print(0)