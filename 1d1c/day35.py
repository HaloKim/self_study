# 17142
import sys
from collections import deque
from itertools import combinations
n,m = map(int, sys.stdin.readline().split())
mat = [[0]*n for _ in range(n)]
for i in range(n):
    mat.append(sys.stdin.readline().split())
mov_x = [-1,0,0,1]
mov_y = [0,-1,1,0]

def bfs(a,b):
    visit = [[0]*n for _ in range(n)]
    queue = deque()
    queue.append([a,b])
    while queue:
        a,b = queue.pop(0)
        for i in range(4):
            a += mov_x[i]
            b += mov_y[i]
            if a < 0 and b < 0 and a >= n and b >= n:
                continue    
virus = []
active = 0
time = 0
cnt = 0

def dfs(cnt):
    if cnt == m:
        bfs()
        return
    else:
        for i in range(len(virus)):
            dfs(cnt+1)
        
for i in range(n):
    for j in range(n):
        if mat[i][j] == 2:
            virus.append([i,j])
        if mat[i][j] == 0:
            active += 1