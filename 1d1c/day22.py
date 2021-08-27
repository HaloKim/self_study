n = int(input())
mat = []
for _ in range(n):
    temp = input()
    mat.append(list(temp))

visit = [[0]*n for _ in range(n)]
x_list = [-1,0,0,1]
y_list = [0,-1,1,0]
def bfs(a,b):
    queue = []
    queue.append([a,b])
    visit[a][b] = 1
    while queue:
        v = queue.pop(0)
        a, b = v
        for k in range(4):
            x = a + x_list[k]
            y = b + y_list[k]
            if x < 0 or x >= n or y < 0 or y >= n:
                continue
            if mat[x][y] == mat[a][b] and visit[x][y] == 0:
                visit[x][y] = 1
                queue.append([x,y])
count = 0
for i in range(n):
    for j in range(n):
        if visit[i][j] == 0:
            bfs(i,j)
            count += 1
print(count)

count = 0
visit = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if mat[i][j] == 'G':
            mat[i][j] = 'R'
for i in range(n):
    for j in range(n):
        if visit[i][j] == 0:
            bfs(i,j)
            count += 1
print(count)