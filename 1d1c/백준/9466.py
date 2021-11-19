import sys
sys.setrecursionlimit(int(1e9))
T = int(input())

def dfs(v):
    global ans
    visit[v] = 1
    cycle.append(v)
    next = arr[v]

    if visit[next] == 1:
        if next in cycle:
            ans += cycle[cycle.index(next):]
        return
    else:
        dfs(next)

for _ in range(T):
    n = int(input())
    visit = [0]*(n+1)
    arr = [0] + list(map(int,input().split()))
    ans = []
    for index in range(1, n+1):
        if visit[index] == 0:
            cycle = []
            dfs(index)
    print(n - len(ans))