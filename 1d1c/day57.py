# 2468
import sys
from collections import deque

n = int(sys.stdin.readline())

area = []
move = [(1,0),(-1,0),(0,1),(0,-1)]

for i in range(n):
    area.append(list(map(int,sys.stdin.readline().strip().split())))

maxi = max(map(max, area))
mini = min(map(min, area))

def bfs(a,b,w):
    q = deque()
    q.append([a,b])
    visit[a][b] = 1
    while q:
        a,b = q.popleft()
        for x,y in move:
            dx = a + x
            dy = b + y
            if 0 <= dx < n and 0 <= dy < n:
                if visit[dx][dy] == 0 and area[dx][dy] >= w:
                    visit[dx][dy] = 1
                    q.append([dx,dy])

ans = 0
for w in range(mini, maxi+1):
    cnt = 0
    visit = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if area[i][j] >= w and visit[i][j] == 0:
                bfs(i,j,w)
                cnt += 1
    ans = max(ans, cnt)
print(ans)