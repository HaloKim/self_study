# 7569
'''
import sys
from collections import deque

m,n,h = map(int, sys.stdin.readline().split())
box = [[[0]*m for _ in range(n)] for _ in range(h)]

for i in range(h):
    for j in range(n):
        box[i][j] = list(map(int,sys.stdin.readline().split()))

dz = [1,-1,0,0,0,0]
dx = [0,0,0,0,1,-1]
dy = [0,0,1,-1,0,0]
q = deque()

for i in range(h):
    for j in range(n):
        for k in range(m):
            if box[i][j][k] == 1:
                q.append([i,j,k])

def bfs():
    while q:
        a,b,c = q.popleft()
        for i in range(6):
            z = a + dz[i]
            x = b + dx[i]
            y = c + dy[i]
            if x < 0 or y < 0 or z < 0 or z > h-1 or x > n-1 or y > m-1:
                continue
            if box[z][x][y] == 0:
                box[z][x][y] = box[a][b][c] + 1
                q.append([z,x,y])
bfs()
mx = 0
for i in range(h):
    for j in range(n):
        for k in range(m):
            if box[i][j][k] == 0:
                print('-1')
                exit()
            mx = max(box[i][j][k], mx)
print(mx-1)
'''

# 1697
import sys
from collections import deque

n,k = map(int,sys.stdin.readline().split())
visit = [0]*(10**5+1)

def bfs(n):
    q = deque()
    q.append(n)
    visit[n] += 1
    while q:
        n = q.popleft()
        for i in (n*2, n+1, n-1):
            if i == k:
                print(visit[n])
                return
            if 0 <= i <= (10**5) and visit[i] == 0:
                q.append(i)
                visit[i] = visit[n] + 1
if n != k:
    bfs(n)
else:
    print(0)