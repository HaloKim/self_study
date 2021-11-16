import sys
sys.setrecursionlimit(int(1e9))
input = sys.stdin.readline

M,N = map(int, input().split())
arr = []
for i in range(M):
    arr.append(list(map(int, input().split())))
dp = [[-1]*N for _ in range(M)]
dp[-1][-1] = 1

def dfs(x,y):
    if dp[x][y] != -1:
        return dp[x][y]

    cnt = 0
    for a,b in (1,0),(0,1),(-1,0),(0,-1):
        dx = x + a
        dy = y + b
        if 0 <= dx < M and 0 <= dy < N:
            if arr[x][y] > arr[dx][dy]:
                cnt += dfs(dx,dy)
    dp[x][y] = cnt
    return dp[x][y]

print(dfs(0,0))