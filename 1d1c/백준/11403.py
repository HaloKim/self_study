n = int(input())
arr = []
visit = [0]*n
for i in range(n):
    arr.append(list(map(int, input().split())))
    
def dfs(v):
    for i in range(n):
        if visit[i] == 0 and arr[v][i] == 1:
            visit[i] = 1
            dfs(i)

for i in range(n):
    dfs(i)
    print(*visit)
    visit = [0]*n