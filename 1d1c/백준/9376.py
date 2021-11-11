from collections import deque
from sys import stdin
input = stdin.readline

T = int(input().strip())
h,w = map(int, input().strip().split())
prizon = []
p1 = []
p2 = []
q = deque()
move = [[1,0],[-1,0],[0,1],[0,-1]]
def bfs(visit,cnt):
    while q:
        x,y = q.popleft()
        for a,b in move:
            dx = a + x
            dy = b + y
            if 0 <= dx < h and 0 <= dy < w:
                if visit[dx][dy] == 0:
                    if x == h-1 and y == w-1:
                        return
                    if prizon[dx][dy] == '#':
                        cnt += 1
                        visit[dx][dy] = visit[x][y] + 1
                    if prizon[dx][dy] == '.':
                        visit[dx][dy] = visit[x][y]
                    q.append([dx,dy])

start = []
for _ in range(T):
    visit = [[0]*w for _ in range(h)]
    for i in range(h):
        temp = input().strip()
        for j in range(len(temp)):
            if '$' == temp[j]:
                start.append([i,j])
                visit[i][j] = 1
        prizon.append(list(temp))
    cnt = 0
    bfs(start[0][0],start[0][1],visit,cnt)
    bfs(start[1][0],start[1][1],visit,cnt)
    print(visit)