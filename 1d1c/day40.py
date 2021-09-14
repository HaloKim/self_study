# 2667 오름차순.. 문제를 잘읽자 !!!
import sys 
from collections import deque
n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    arr.append([int(i) for i in sys.stdin.readline().strip()])
visit = [[0]*n for _ in range(n)]
movx = [0,1,0,0,-1]
movy = [0,0,1,-1,0]

def bfs(a,b):
    cnt = 0
    q = deque()
    q.append([a,b])
    while q:
        a,b = q.popleft()
        for i in range(5):
            x = a + movx[i]
            y = b + movy[i]
            if x < 0 or y < 0 or x > n-1 or y > n-1:
                continue
            if visit[x][y] == 0 and arr[x][y] == 1 and arr[a][b] == 1:
                visit[x][y] = 1
                q.append([x,y])
                cnt += 1
    return cnt
total_cnt = 0
ans = []
for i in range(n):
    for j in range(n):
        if visit[i][j] == 0:
            tmp = bfs(i,j)
            if tmp:
                ans.append(tmp)
                total_cnt += 1
print(total_cnt)
ans.sort()
print(*ans, sep='\n')