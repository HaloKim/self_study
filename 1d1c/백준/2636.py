from collections import deque
from sys import stdin
input = stdin.readline

r,c = map(int,input().strip().split())
box = []
for _ in range(r):
    box.append(list(input().strip().split()))

ans = []
def bfs():
    q = deque()
    q.append([0,0])
    visit = [[0]*c for _ in range(r)]
    visit[0][0] = 1
    cnt = 0
    while q:
        x,y = q.popleft()
        for a,b in (1,0),(-1,0),(0,1),(0,-1):
            dx = x + a
            dy = y + b
            if 0 <= dx < r and 0 <= dy < c and visit[dx][dy] == 0:
                if box[dx][dy] == '0':
                    q.append([dx,dy])
                    visit[dx][dy] = 1
                elif box[dx][dy] == '1':
                    box[dx][dy] = '0'
                    visit[dx][dy] = 1
                    cnt += 1
    ans.append(cnt)
    return cnt
                
time = 0
while True:
    time += 1
    cnt = bfs()
    if cnt == 0:
        break
print(time-1)
print(ans[-2])