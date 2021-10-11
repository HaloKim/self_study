# 1260 복습
n, m, v = map(int, input().split())
mat = [[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    mat[x][y] = mat[y][x] = 1
visit = [0]*(n+1)
def dfs(v):
    print(v, end=" ")
    visit[v] = 1
    for i in range(1,n+1):
        if visit[i] == 0 and mat[v][i] == 1:
            dfs(i)
def bfs(v):
    queue = [v]
    visit[v] = 0
    while queue:
        print(queue)
        v = queue.pop(0)
        print(v, end=" ")
        for i in range(1,n+1):
            if visit[i] == 1 and mat[v][i] == 1:
                queue.append(i)
                visit[i] = 0
dfs(v)
print()
bfs(v)