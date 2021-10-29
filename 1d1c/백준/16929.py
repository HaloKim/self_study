N, M = map(int, input().split())

visit = [[0]*M for _ in range(N)]

board = []
for _ in range(N):
    board.append(list(input()))

move = [[-1,0],[0,1],[1,0],[0,-1]]

def dfs(x,y,sx,sy,check,color):
    for a,b in move:
        dx = x + a
        dy = y + b
        if 0 <= dx < N and 0 <= dy < M:
            if check >= 4 and dx == sx and dy == sy:
                print("Yes")
                exit()
            if visit[dx][dy] == 0 and color == board[dx][dy]:
                visit[dx][dy] = 1
                dfs(dx, dy, sx, sy, check+1, color)
                visit[dx][dy] = 0
    return

for i in range(N):
    for j in range(M):
        visit[i][j] = 1
        dfs(i,j,i,j,1,board[i][j])

print('No')