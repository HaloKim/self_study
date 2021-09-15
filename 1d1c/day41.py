# 1012
import sys
from collections import deque

movex = [1,0,0,-1]
movey = [0,-1,1,0]
global visit

def bfs(a,b):
    q = deque()
    q.append([a,b])
    visit[a][b] = 1
    while q:
        a,b = q.popleft()
        for i in range(4):
            x = movex[i] + a
            y = movey[i] + b
            if x < 0 or y < 0 or x > m-1 or y > n-1:
                continue
            if visit[x][y] == 0 and mat[x][y] == 1:
                visit[x][y] = 1
                q.append([x,y])

tmp = int(sys.stdin.readline())
for _ in range(tmp):
    m,n,k = map(int,sys.stdin.readline().split())
    mat = [[0]*n for _ in range(m)]
    visit = [[0]*n for _ in range(m)]
    for i in range(k):
        a,b = map(int,sys.stdin.readline().split())
        mat[a][b] = 1
    cnt = 0
    for i in range(m):
        for j in range(n):
            if visit[i][j] == 0 and mat[i][j] == 1:
                bfs(i,j)
                cnt += 1
    print(cnt)