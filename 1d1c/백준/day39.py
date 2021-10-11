# 1260
'''
import sys
from collections import deque

n,m,v = map(int,sys.stdin.readline().split())
mat = [[0]*(n+1) for _ in range(n+1)]
dvisit = [0]*(n+1)
bvisit = [0]*(n+1)
for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())
    mat[a][b] = mat[b][a] = 1

def dfs(v):
    dvisit[v] = 1
    print(v, end=' ')
    for i in range(1,n+1):
        if dvisit[i] == 0 and mat[v][i] == 1:
            dfs(i)
def bfs(v):
    q = deque()
    q.append(v)
    bvisit[v] = 1
    while q:
        v = q.popleft()
        print(v, end=' ')
        for i in range(1, n+1):
            if bvisit[i] == 0 and mat[i][v] == 1:
                bvisit[i] = 1
                q.append(i)
dfs(v)
print()
bfs(v)
'''

# 2606
'''
import sys
from collections import deque

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
visit = [0]*(n+1)
mat = [[0]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())
    mat[a][b] = mat[b][a] = 1

def dfs(v):
    visit[v] = 1
    for i in range(1,1+n):
        if mat[v][i] == 1 and visit[i] == 0:
            dfs(i)
dfs(1)

def bfs(v):
    q = deque()
    q.append(v)
    visit[v] = 1
    while q:
        v = q.popleft()
        for i in range(1,1+n):
            if visit[i] == 0 and mat[v][i] == 1:
                visit[i] = 1
                q.append(i)
    print(visit)
    
bfs(1)
print(sum(visit)-1)
'''
'''
35
30
14 16
12 22
11 14
11 12
5 18
6 31
7 21
29 34
4 9
15 27
2 27
25 32
1 5
2 32
18 26
26 27
3 25
12 24
16 24
1 2
12 29
20 31
17 20
6 12
13 22
5 34
14 15
4 26
22 28
16 18
'''

