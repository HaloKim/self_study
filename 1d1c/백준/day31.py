# 5567 쉽게 풀수있다.
'''
n = int(input())
m = int(input())
arr = [[0] for i in range(m)]
for i in range(m):
    arr[i] = list(map(int,input().split()))
visit = [[0]*(n+1) for i in range(n+1)]

def bfs(a,b):
    queue = []
    visit[a][b] = 1
    visit[b][a] = 1
    queue.append([a,b])
    while queue:
        x,y = queue.pop(0)
        if visit[x][y] == 0:
            visit[x][y] = 1
            visit[y][x] = 1
            queue.append([x,y])
for i in range(m):
    bfs(arr[i][0],arr[i][1])

temp = [0]*(n+1)
while(n):
    for i in range(1,len(visit[1])):
        if visit[1][i] == 1:
            temp[i] = 1
            for j in range(2,len(visit[i])):
                if visit[i][j] == 1 and visit[1][j] == 0:
                    temp[j] = 1
    n -= 1
print(sum(temp))
'''
def bfs(x):
    queue = []
    visit = [0] * (n+1)
    visit[x] = 1
    queue.append(x)
    while queue:
        v = queue.pop(0)
        for i in arr[v]:
            if visit[i] == 0:
                visit[i] = visit[v] + 1
                queue.append(i)
    return visit

n = int(input())
m = int(input())
arr = [[] for i in range(n+1)]
for i in range(m):
    a,b = map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)
visit = bfs(1)
cnt = 0
for i in visit:
    if 1 < i and i <= 3:
        cnt += 1
print(cnt)