# 17141
import sys
from collections import deque
import copy
n,m = map(int, sys.stdin.readline().split())
mat = [[0]*n for _ in range(n)]
for i in range(n):
    mat.append(sys.stdin.readline().split())
cmat = copy.deepcopy(mat)
mov_x = [-1,0,0,1]
mov_y = [0,-1,1,0]
virus = []
select = [0 for _ in range(m)]
active = 0
time = 0

def bfs(queue):
    while queue:
        a,b = queue.popleft()
        for i in range(4):
            x = a + mov_x[i]
            y = b + mov_y[i]
            if a < 0 and b < 0 and a >= n and b >= n:
                continue
            else:
                if mat[x][y] == 0:
                    queue.append([x,y])

def dfs(index, cnt):
    if cnt == m:
        queue = deque()
        for i in range(cnt):
            if select[i] == 1:
                queue.append(virus[i])
        bfs(queue)
        return
    else:
        for i in range(len(virus)):
            if select[i]:
                continue
            select[i] = 1
            dfs(i,cnt+1)
            select[i] = 0
        
for i in range(n):
    for j in range(n):
        if mat[i][j] == 2:
            virus.append([i,j])
        if mat[i][j] == 0:
            active += 1

dfs(0,0)