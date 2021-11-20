from collections import deque
from sys import stdin
input = stdin.readline

R,C = map(int, input().strip().split())
visit = [[0]*C for _ in range(R)]
arr = []
for i in range(R):
    arr.append(list(input().strip()))

def water():
    qlen = len(w) # 최초 갖고 있던 물의 갯수
    while qlen:
        x,y = w.popleft()
        for a,b in (0,1),(1,0),(-1,0),(0,-1):
            dx = x + a
            dy = y + b
            if 0 <= dx < R and 0 <= dy < C:
                if arr[dx][dy] == '.':
                    arr[dx][dy] = '*'
                    w.append([dx,dy])
        qlen -= 1

def doch(x,y):
    q = deque()
    q.append([x,y])
    visit[x][y] = 1
    while q:
        qlen = len(q) # 최초 갖고있던 도치위치
        while qlen:
            x,y = q.popleft()
            for a,b in (0,1),(1,0),(-1,0),(0,-1):
                dx = x + a
                dy = y + b
                if 0 <= dx < R and 0 <= dy < C:
                    if arr[dx][dy] == 'D':
                        return visit[x][y]
                    elif visit[dx][dy] == 0 and arr[dx][dy] == '.':
                        q.append([dx,dy])
                        visit[dx][dy] = visit[x][y] + 1
            qlen -= 1
        water()
    return 0

w = deque()
for i in range(R):
    for j in range(C):
        if arr[i][j] == '*':
            w.append([i,j])
            continue
        if arr[i][j] == 'S':
            d = [i,j]
water()
x,y = d
ans = doch(x,y)
if ans > 0:
    print(ans)
else:
    print("KAKTUS")