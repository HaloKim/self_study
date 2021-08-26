import copy

n, m = map(int, input().split())
mat = [[0] for _ in range(m)]

for i in range(n):
    mat[i] = list(map(int,input().split()))

empty = []
for i in range(n):
    for j in range(m):
        if mat[i][j] == 0:
            empty.append([i,j])

def bfs(arr):
    return

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
            