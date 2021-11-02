import sys
sys.setrecursionlimit(10000)
M, N, K = map(int, input().split())
paper = [[0]*N for _ in range(M)]
for _ in range(K):
    a,b,c,d = map(int, input().split())
    for i in range(b,d):
        for j in range(a, c):
            paper[i][j] = 1

move = [(1,0),(0,1),(-1,0),(0,-1)]
def dfs(x,y,cnt):
    paper[x][y] = 1
    for a,b in move:
        dx = x + a
        dy = y + b
        if 0 <= dx < M and 0 <= dy < N and paper[dx][dy] == 0:
            cnt = dfs(dx,dy,cnt+1)
    return cnt

ans = []
for i in range(M):
    for j in range(N):
        if paper[i][j] == 0:
            ans.append(dfs(i,j,1))
print(len(ans))
print(*sorted(ans))