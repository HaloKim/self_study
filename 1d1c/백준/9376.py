from collections import deque
from sys import stdin
input = stdin.readline

def bfs(x, y):
    visit = [[-1] * (w + 2) for _ in range(h + 2)]
    q.append([x, y])
    visit[x][y] = 0
    while q:
        x, y = q.popleft()
        for a,b in (1,0),(-1,0),(0,1),(0,-1):
            nx = x + a
            ny = y + b
            if 0 <= nx < h+2 and 0 <= ny < w+2:
                if visit[nx][ny] == -1:
                    if maze[nx][ny] == '.':
                        visit[nx][ny] = visit[x][y]
                        q.appendleft([nx, ny])
                    elif maze[nx][ny] == '#':
                        visit[nx][ny] = visit[x][y] + 1
                        q.append([nx, ny])
    return visit

def new_map():
    for i in maze:
        i.insert(0, '.')
        i.append('.')
    maze.insert(0, ['.' for _ in range(w+2)])
    maze.append(['.' for _ in range(w+2)])

for _ in range(int(input())):
    h, w = map(int, input().split())
    maze = [list(input().strip()) for _ in range(h)]
    q = deque()

    new_map()

    temp = []
    for i in range(h + 2):
        for j in range(w + 2):
            if maze[i][j] == '$':
                temp.extend([i, j])
                maze[i][j] = '.'

    x1, y1, x2, y2 = temp
    c1 = bfs(0, 0)
    c2 = bfs(x1, y1)
    c3 = bfs(x2, y2)

    ans = int(1e9)
    for i in range(h+2):
        for j in range(w+2):
            if c1[i][j] != -1 and c2[i][j] != -1 and c3[i][j] != -1:
                cnt = c1[i][j] + c2[i][j] + c3[i][j]
                if maze[i][j] == '#':
                    cnt -= 2
                ans = min(ans, cnt)
    print(ans)