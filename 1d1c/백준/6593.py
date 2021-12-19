from collections import deque
from sys import stdin
input = stdin.readline

def bfs(visit,s):
    move = [
        (-1,0,0),
        (0,0,1),(0,1,0),(0,0,-1),(0,-1,0),
        (1,0,0)]
    l,r,c = s
    q = deque()
    q.append(s)
    visit[l][r][c] = 1
    while q:
        l,r,c = q.popleft()
        for x,y,z in move:
            nl,nr,nc = l+x, r+y, c+z
            if 0 <= nl < L and 0 <= nr < R and 0 <= nc < C and visit[nl][nr][nc] == 0:
                if building[nl][nr][nc] == 'E':
                    return visit[l][r][c]
                if building[nl][nr][nc] == '.':
                    visit[nl][nr][nc] = visit[l][r][c] + 1
                    q.append((nl,nr,nc))
    return

while True:
    L,R,C = map(int,input().strip().split())
    start = (0,0,0)
    if (L,R,C) == (0,0,0):
        break
    building = [[] for _ in range(L)]
    visit = [[[0]*C for _ in range(R)] for _ in range(L)]
    for i in range(L):
        for j in range(R):
            tmp = list(input().strip())
            if 'S' in tmp:
                start = tmp.index('S')
                start = (i,j,start)
            building[i].append(tmp)
        input()
    ans = bfs(visit,start)
    if ans:
        print('Escaped in %d minute(s).' %(ans))
    else:
        print('Trapped!')
