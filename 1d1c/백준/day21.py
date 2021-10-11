# 14502
import copy

n, m = map(int, input().split())
mat = [[0] for _ in range(n)]

for i in range(n):
    mat[i] = list(map(int,input().split()))

empty = []
virus = []
for i in range(n):
    for j in range(m):
        if mat[i][j] == 0:
            empty.append([i,j])
        if mat[i][j] == 2:
            virus.append([i,j])

maximum = 0
x_compare = [-1, 0, 0, 1]
y_compare = [0, -1, 1, 0]
def bfs(arr):
    visit = [[0]*m for _ in range(n)]
    queue = copy.deepcopy(virus)

    count = 0
    global maximum

    while queue:
        x, y = queue.pop(0)
        for i in range(4):
            nx = x + x_compare[i]
            ny = y + y_compare[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if arr[nx][ny] == 0 and visit[nx][ny] == 0:
                arr[nx][ny] = 2
                visit[nx][ny] = 1
                queue.append([nx,ny])

    for i in range(len(arr)):
        count += arr[i].count(0)

    if count > maximum:
        maximum = count

for i in range(len(empty)-2):
    for j in range(i+1,len(empty)):
        for k in range(j+1, len(empty)):
            temp = copy.deepcopy(mat)

            x,y = empty[i]
            temp[x][y] = 1

            x,y = empty[j]
            temp[x][y] = 1

            x,y = empty[k]
            temp[x][y] = 1

            bfs(temp)

print(maximum)