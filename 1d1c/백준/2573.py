from collections import deque
from sys import stdin
input = stdin.readline

N,M = map(int,input().split())

ice = [list(map(int, input().strip().split())) for _ in range(N)]

move = [[0,1],[0,-1],[1,0],[-1,0]]
def melt(a,b):
    q = deque()
    q.append([a,b])
    visit[a][b] = 1
    while q:
        cnt = 0
        x,y = q.popleft()
        for a,b in move:
            dx = x + a
            dy = y + b
            if 0 <= dx < N and 0 <= dy < M:
                if ice[dx][dy] <= 0 and visit[dx][dy] == 0:
                    cnt += 1
                if visit[dx][dy] == 0 and ice[dx][dy] > 0:
                    visit[dx][dy] = 1
                    q.append([dx,dy])
        ice[x][y] -= cnt

def lump(a,b):
    q = deque()
    q.append([a,b])
    visit[a][b] = 1
    while q:
        x,y = q.popleft()
        for a,b in move:
            dx = x + a
            dy = y + b
            if 0 <= dx < N and 0 <= dy < M:
                if visit[dx][dy] == 0 and ice[dx][dy] > 0:
                    visit[dx][dy] = 1
                    q.append([dx,dy])

year = 0
# 녹이기
while True:
    no_ans = 0
    # 덩어리세기
    cnt_lump = 0
    visit = [[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if ice[i][j] > 0 and visit[i][j] == 0:
                lump(i,j)
                cnt_lump += 1
    if cnt_lump > 1:
        print(year)
        break

    visit = [[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if ice[i][j] > 0 and visit[i][j] == 0:
                melt(i,j)
                no_ans += 1
                year += 1
    if no_ans == 0:
        print(0)
        break