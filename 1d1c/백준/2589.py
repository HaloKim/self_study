from collections import deque
from sys import stdin
input = stdin.readline

a,b = map(int, input().strip().split())
land = []
for _ in range(a):
    land.append(list(input().strip()))

def bfs(x,y,maxi):
    q = deque()
    q.append([x,y])
    visit[x][y] = 1
    while q:
        x,y = q.popleft()
        for aa,bb in (1,0),(0,1),(-1,0),(0,-1):
            dx = x + aa
            dy = y + bb
            if 0 <= dx < a and 0 <= dy < b:
                if visit[dx][dy] == 0 and land[dx][dy] == 'L':
                    visit[dx][dy] = visit[x][y] + 1
                    maxi = max(maxi, visit[x][y] + 1)
                    q.append([dx,dy])
    return maxi
maxi = 0
for i in range(a):
    for j in range(b):
        if land[i][j] == 'L':
            visit = [[0]*b for _ in range(a)]
            maxi = bfs(i,j,maxi)
print(maxi-1)