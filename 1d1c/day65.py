# 3197
from collections import deque
import sys

input = sys.stdin.readline
R,C = map(int,input().split())
lake, loc = [], []

for i in range(R):
    lake.append(list(input().strip()))
    for j in range(C):
        if lake[i][j] == 'L':
            loc.append([i,j])

move = ((0,1),(0,-1),(1,0),(-1,0))
wc = [[False]*C for _ in range(R)]
sc = [[False]*C for _ in range(R)]
wq1, wq2 = deque(), deque()
sq1, sq2 = deque(), deque()

for i in range(R):
    for j in range(C):
        if lake[i][j] == 'L':
            if not sq1:
                sq1.append((i, j))
                sc[i][j] = 1
            else:
                ex, ey = i, j
            lake[i][j] = '.'
        if lake[i][j] == '.':
            wq1.append((i, j))
            wc[i][j] = 1

def melt():
    while wq1:
        x, y = wq1.popleft()
        lake[x][y] = '.'
        for a,b in move:
            nx, ny = x+a, y+b
            if nx < 0 or nx >= R or ny < 0 or ny >= C or wc[nx][ny]:
                continue
            if lake[nx][ny] == '.':
                wq1.append((nx, ny))
            else:
                wq2.append((nx, ny))
            wc[nx][ny] = 1

def swan():
    while sq1:
        x, y = sq1.popleft()
        if x == ex and y == ey:
            return 1
        for a,b in move:
            nx, ny = x+a, y+b
            if nx < 0 or nx >= R or ny < 0 or ny >= C or sc[nx][ny]:
                continue
            if lake[nx][ny] == '.':
                sq1.append((nx, ny))
            else:
                sq2.append((nx, ny))
            sc[nx][ny] = 1
    return False

ans = 0
while True:
    melt()
    if swan():
        break
    wq1 = wq2
    sq1 = sq2
    wq2 = deque()
    sq2 = deque()
    ans += 1
print(ans)