# 2933
from collections import deque
import sys
input = sys.stdin.readline
R,C = map(int, input().split())
cave = [list(input()) for _ in range(R)]
N = int(input())
cnt = map(int, input().split())

left = 1
mov = [(0,1),(0,-1),(1,0),(-1,0)]

def fallen(visit, fall):
    down, stop = 1, 0
    while True:
        for x, y in fall:
            if x + down == R-1: # 끝지점
                stop = 1
                break
            if cave[x+down+1][y] == 'x' and visit[x+down+1][y] == 0: # 미네랄이면
                stop = 1
                break
        if stop:
            break
        down += 1

    for i in range(R-2, -1, -1):
        for j in range(C):
            if cave[i][j] == 'x' and visit[i][j]:
                cave[i][j] = '.'
                cave[i+down][j] = 'x'

def bfs(a,b):
    q = deque()
    q.append([a,b])
    visit = [[0]*C for _ in range(R)]
    visit[a][b] = 1

    while q:
        x,y = q.popleft()
        fall = []
        if x == R-1:
            return
        if cave[x+1][y] == '.':
            fall.append([x,y])
        for a,b in mov:
            dx = x + a
            dy = y + b
            if 0 <= dx < R and 0 <= dy < C:
                if cave[dx][dy] == 'x' and visit[dx][dy] == 0:
                    visit[dx][dy] = 1
                    q.append([dx,dy])
    fallen(visit, fall)
    return

for i in cnt:
    if left:
        for j in range(C):
            if cave[-i][j] == 'x':
                cave[-i][j] = '.'
                break
        for j in range(R):
            for k in range(C):
                if cave[j][k] == 'x':
                    bfs(j,k)
        left = 0
    else:
        for j in range(C-1,-1,-1):
            if cave[-i][j] == 'x':
                cave[-i][j] = '.'
                break
        for j in range(R):
            for k in range(C):
                if cave[j][k] == 'x':
                    bfs(j,k)
        left = 1
for i in range(R):
    for j in range(C):
        print(cave[i][j], end='')
    print()