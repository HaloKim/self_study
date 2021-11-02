from collections import deque
import sys
sys.setrecursionlimit(int(1e9))
input = sys.stdin.readline

forest = []
n = int(input())
forest = [list(map(int, input().split())) for _ in range(n)]
move = ((1,0),(-1,0),(0,1),(0,-1))

def dfs(x,y):
    if visit[x][y]:
        return visit[x][y]
    visit[x][y] = 1
    for a,b in move:
        dx = x + a
        dy = y + b
        if 0 <= dx < n and 0 <= dy < n:
            if forest[dx][dy] > forest[x][y]:
                visit[x][y] = max(visit[x][y], dfs(dx, dy)+1)
    return visit[x][y]

cnt = 0
visit = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        cnt = max(cnt, dfs(i,j))
print(cnt)