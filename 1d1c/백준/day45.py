# 7562
import sys
from collections import deque

n = int(sys.stdin.readline())

mov = [(-2, 1), (-1, 2), (1, 2), (2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]

def bfs(a,b,i):
    q = deque()
    q.append([a,b])
    board[a][b] = 1
    while q:
        x,y = q.popleft()
        for dx,dy in mov:
            movx = x + dx
            movy = y + dy
            if 0 <= movx < i and 0 <= movy < i:
                if board[movx][movy] == 0:
                    q.append([movx,movy])
                    board[movx][movy] = board[x][y] + 1
                if movx == ex and movy == ey:
                    return board[movx][movy]-1
    return
        
for _ in range(n):
    i = int(sys.stdin.readline())
    board = [[0]*i for _ in range(i)]
    sx,sy = map(int, sys.stdin.readline().split()) # start
    ex,ey = map(int, sys.stdin.readline().split()) # end
    print(bfs(sx,sy,i))