# 2187
'''
import sys
from collections import deque

n,m = map(int,sys.stdin.readline().split())
mat = []

for _ in range(n):
    mat.append([i for i in map(int, sys.stdin.readline().strip())])
dx = [0,0,1,-1]
dy = [-1,1,0,0]
visit = [[0]*m for _ in range(n)]
minimum = n*m
cnt = 0

def bfs(a,b):
    global cnt
    global minimum
    q = deque()
    q.append([a,b])
    visit[a][b] = 1

    while q:
        a,b = q.popleft()
        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]
            if x < 0 or y < 0 or x > n-1 or y > m-1:
                continue
            if mat[x][y] != 0 and visit[x][y] == 0:
                cnt += 1
                visit[x][y] = visit[a][b]+1
                q.append([x,y])

for i in range(n):
    for j in range(m):
        if mat[i][j] == 1 and visit[i][j] == 0:
            bfs(i,j)
print(visit[-1][-1])
'''
# 7576
import sys
from collections import deque
n,m = map(int, sys.stdin.readline().split())
box = []
for _ in range(m):
    box.append(list(map(int, sys.stdin.readline().split())))
visit = [[0]*n for i in range(m)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(a,b):
    global visit
    q = deque()
    q.append([a,b])
    visit[a][b] = 1
    while q:
        a,b = q.popleft()
        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]
            if x < 0 or y < 0 or x > m-1 or y > n-1:
                continue
            if visit[x][y] == 0 and box[x][y] == 0:
                print(x,y)
                visit[x][y] = 1
                for j in range(4):
                    xx = x + dx[j]
                    yy = y + dy[j]
                    if xx < 0 or yy < 0 or xx > m-1 or yy > n-1:
                        continue
                    if box[xx][yy] > 0:
                        box[x][y] = min(box[a][b] + 1, box[xx][yy]+1)
                q.append([x,y])

for i in range(m):
    for j in range(n):
        if box[i][j] == 1 and visit[i][j] == 0:
            bfs(i,j)
print(box)