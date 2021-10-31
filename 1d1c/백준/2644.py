N = int(input())
A, B = map(int,input().split())
M = int(input())
fam = [[] for _ in range(N+1)]

for _ in range(M):
    a,b = map(int, input().split())
    fam[a].append(b)
    fam[b].append(a)

visit = [0]*(N+1)
def dfs(node):
    for n in fam[node]:
        if visit[n] == 0:
            visit[n] = visit[node] + 1
            dfs(n)
dfs(A)
print(visit[B] if visit[B] > 0 else -1)