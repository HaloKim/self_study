# 1922
n = int(input())
m = int(input())
arr = []
for i in range(m):
    arr.append(list(map(int, input().split())))
arr.sort(key=lambda x: x[-1])
def bfs(a):
    queue = []
    queue.append([x,y])
    visit = [[0]*2 for i in range(m)]
bfs()