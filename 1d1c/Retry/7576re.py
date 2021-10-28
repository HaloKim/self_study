from collections import deque

M,N = map(int, input().split())
box = []
q = deque()
mov = [[1,0],[-1,0],[0,1],[0,-1]]
for i in range(N):
    box.append(list(map(int, input().split())))

for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            q.append([i,j])

def bfs():
    global ans
    while q:
        x,y = q.popleft()
        for a,b in mov:
            dx = x + a
            dy = y + b
            if 0 <= dx < N and 0 <= dy < M:
                if box[dx][dy] == 0:
                    box[dx][dy] = box[x][y] + 1
                    q.append([dx, dy])
bfs()

ans = 0
for i in range(N):
    for j in range(M):
        if box[i][j] == 0:
            print(-1)
            exit()
        ans = max(ans,box[i][j])
print(ans-1)