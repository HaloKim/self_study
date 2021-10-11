# 13460 매우어렵다
import sys
from collections import deque

n,m = map(int, sys.stdin.readline().strip().split())

board = []
move  = [(1,0),(0,1),(-1,0),(0,-1)]

for i in range(n):
    board.append(list(sys.stdin.readline().strip()))
    for j in range(m):
        if board[i][j] == 'R':
            rx,ry = i,j
        if board[i][j] == 'B':
            bx,by = i,j

# 끝까지 이동하는 함수
def moving(x,y,addx,addy):
    while True:
        x += addx
        y += addy
        if board[x][y] == '#':
            x -= addx
            y -= addy
            break
        if board[x][y] == 'O':
            break
    return x,y

# 그래프탐색
def bfs(rx,ry,bx,by,cnt):
    # init
    q = deque()
    q.append((rx,ry,bx,by,cnt))
    visit = []
    visit.append((rx,ry,bx,by))

    while q:
        rx,ry,bx,by,cnt = q.popleft()
        if cnt == 11:
            print(-1)
            return
        if board[rx][ry] == 'O':
            print(cnt)
            return
        for x,y in move:
            nrx, nry = moving(rx,ry,x,y)
            nbx, nby = moving(bx,by,x,y)
            if board[nbx][nby] == 'O':
                continue
            if nrx == nbx and nry == nby:
                if abs(nrx-rx) + abs(nry-ry) > abs(nbx-bx) + abs(nby-by):
                    nrx -= x
                    nry -= y
                else:
                    nbx -= x
                    nby -= y
            if (nrx,nry,nbx,nby) not in visit:
                q.append((nrx,nry,nbx,nby,cnt+1))
                visit.append((nrx,nry,nbx,nby))
    print(-1)

bfs(rx,ry,bx,by,0)