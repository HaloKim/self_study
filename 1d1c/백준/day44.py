# 2206
import sys
from collections import deque

n,m = map(int, sys.stdin.readline().split())
mat = []
dx = [0,0,-1,1]
dy = [1,-1,0,0]

for _ in range(n):
    mat.append(list(map(int, sys.stdin.readline().strip())))

def bfs():
    q = deque()
    q.append([0,0,1])
    visit = [[[0]*2 for i in range(m)] for i in range(n)]
    visit[0][0][1] = 1
    while q:
        a,b,w = q.popleft()
        if a == n-1 and b == m-1:
            return visit[a][b][w]
        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]
            if 0 <= x < n and 0 <= y < m:
                if mat[x][y] == 1 and w == 1:
                    visit[x][y][0] = visit[a][b][1] + 1
                    q.append([x,y,0])
                elif visit[x][y][w] == 0 and mat[x][y] == 0:
                    visit[x][y][w] = visit[a][b][w] + 1
                    q.append([x,y,w])
    return -1
print(bfs())