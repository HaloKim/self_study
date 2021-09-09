import sys
from collections import deque
n,m = map(int, sys.stdin.readline().split())
mat = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        mat.append(sys.stdin.readline().split())
mov_x = [-1,0,0,1]
mov_y = [0,-1,1,0]

def bfs():
    visit = [[0]*n for _ in range(n)]
    queue = []
    queue = deque()
active = []
wall = []
for i in range(n):
    for j in range(n):
        if mat[i][j] == 2:
            active.append([i,j])
        if mat[i][j] == 1:
            wall.append([i,j])