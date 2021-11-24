import sys
sys.setrecursionlimit(int(1e9))
N = int(input())
trees = [[] for _ in range(N+1)]
for i in range(1,N+1):
    trees[i].append(int(input()))

def dfs(v,i):
    visit[v] = 1
    for w in trees[v]:
        if visit[w] == 0:
            dfs(w,i)
        elif visit[w] and w == i:
            ans.append(w)
ans = []
for i in range(1, N+1):
    visit = [0]*(N+1)
    dfs(i,i)
print(len(ans))
print(*ans, sep='\n')