# 4963
from collections import deque

move = [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]

def bfs(a,b):
    q = deque()
    q.append([a,b])
    while q:
        a,b = q.popleft()
        for i,j in move:
            x = a + i
            y = b + j
            if 0 <= x < h and 0 <= y < w:
                if visit[x][y] == 0 and island[x][y] == 1:
                    visit[x][y] = 1
                    q.append([x,y])
    return

while(True):
    w,h = map(int,input().split())

    if w == 0:
        break

    cnt = 0
    island = [[0]*w for _ in range(h)]
    visit = [[0]*w for _ in range(h)]

    for i in range(h):
        island[i] = list(map(int, input().split()))
    for i in range(h):
        for j in range(w):
            if island[i][j] == 1 and visit[i][j] == 0:
                bfs(i,j)
                cnt += 1
    print(cnt)