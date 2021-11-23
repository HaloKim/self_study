from sys import stdin
input = stdin.readline

N = int(input())
pipe = [list(map(int, input().strip().split())) for _ in range(N)]
def dfs(x,y,d):
    global cnt
    if x == N-1 and y == N-1:
        cnt += 1
    if d == 0:
        if y+1 < N and pipe[x][y+1] == 0:
            dfs(x,y+1,0)
        if x+1 < N and y+1 < N:
            if pipe[x][y+1] == 0 and pipe[x+1][y] == 0 and pipe[x+1][y+1] == 0:
                dfs(x+1,y+1,2)
    if d == 1:
        if x+1 < N and pipe[x+1][y] == 0:
            dfs(x+1,y,1)
        if x+1 < N and y+1 < N:
            if pipe[x][y+1] == 0 and pipe[x+1][y] == 0 and pipe[x+1][y+1] == 0:
                dfs(x+1,y+1,2)
    if d == 2:
        if y+1 < N and pipe[x][y+1] == 0:
            dfs(x,y+1,0)
        if x+1 < N and pipe[x+1][y] == 0:
            dfs(x+1,y,1)
        if x+1 < N and y+1 < N:
            if pipe[x][y+1] == 0 and pipe[x+1][y] == 0 and pipe[x+1][y+1] == 0:
                dfs(x+1,y+1,2)
cnt = 0
dfs(0,1,0)
print(cnt)