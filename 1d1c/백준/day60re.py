# 3190 재풀이
from collections import deque
n = int(input())
k = int(input())
board = [[0]*n for _ in range(n)]
for i in range(k):
    x,y = map(int,input().split())
    board[x-1][y-1] = 1 # 사과위치

l = int(input())
rotate = {}
for _ in range(l):
    x,c = input().split()
    rotate[int(x)] = c

def change(d, c):
    if c == "L":
        d = (d-1)%4
    else:
        d = (d+1)%4
    return d

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

def dfs():
    direction = 1
    time = 1
    x,y = 0,0
    visit = deque([[x,y]])
    board[x][y] = 2
    while True:
        x,y = x + dx[direction], y + dy[direction]
        if 0 <= y < n and 0 <= x < n and board[x][y] != 2:
            if not board[x][y] == 1:
                tx,ty = visit.popleft()
                board[tx][ty] = 0
            board[x][y] = 2
            visit.append([x,y])
            if time in rotate.keys():
                direction = change(direction, rotate[time])
            time += 1
        else:
            return time
print(dfs())