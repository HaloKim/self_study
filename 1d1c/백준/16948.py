from collections import deque

N = int(input())
r1,c1,r2,c2 = map(int, input().split())
move = [(-2,-1),(-2,1),(0,-2),(0,2),(2,-1),(2,1)]

def bfs():
    q = deque()
    q.append([r1,c1])
    visit = [[0]*(N+1) for _ in range(N+1)]
    visit[r1][c1] = 1
    while q:
        x,y = q.popleft() 
        for a,b in move:
            dx = x + a
            dy = y + b
            if dx == r2 and dy == c2:
                return visit[x][y]
            if 0 <= dx < N and 0 <= dy < N:
                if visit[dx][dy] == 0:
                    visit[dx][dy] = visit[x][y] + 1
                    q.append([dx,dy])
    return -1
print(bfs())