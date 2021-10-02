# 13460
import sys
from collections import deque

n,m = map(int, sys.stdin.readline().strip().split())
board = [list(sys.stdin.readline().strip()) for _ in range(m)]

visit = [[0]*n for _ in range(m)]
move  = [(1,0),(0,1),(-1,0),(0,-1)]

def bfs(a,b,cnt):
    global dr
    chk = 0
    redq = deque()
    redq.append([a,b])
    visit[a][b] = cnt+1
    while redq:
        a,b = redq.popleft()
        if chk == 0:
            for x,y in move:
                dx = x + a
                dy = y + b
                if 0 <= dx < m and 0 <= dy < n:
                    if board[dx][dy] == '.':
                        redq.append(dx,dy)
                        visit[dx][dy] = visit[a][b]
                        chk = (x,y)
                        dr = (dx,dy)
                        print(visit)
                    if board[dx][dy] == 'O':
                        return (dx,dy)
                    if board[dx][dy] == '#':
                        return (dx,dy)
        else:
            dx = x + a
            dy = y + b
            if 0 <= dx < m and 0 <= dy < n:
                if board[dx][dy] == '.':
                    redq.append(dx,dy)
                    visit[dx][dy] = visit[a][b]
                    chk = (x,y)
                    dr = (dx,dy)
                    print(visit)
                if board[dx][dy] == 'O':
                        return (dx,dy)
                if board[dx][dy] == '#':
                    return (dx,dy)

dr = 0
db = 0

for i in range(m):
    for j in range(n):
        if board[i][j] == 'R':
            dr = [i,j]
        if board[i][j] == 'B':
            db = [i,j]

cnt = 0
while True:
    cnt += 1
    a,b = bfs(dr[0],dr[1], cnt)
    if board[a][b] == 'O':
        print(visit[a][b])
        break