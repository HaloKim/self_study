import sys
sys.setrecursionlimit(int(1e9))
input = sys.stdin.readline

n = int(input())
trees = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b,c = map(int, input().split())
    trees[a].append((b,c))
    trees[b].append((a,c))

def dfs(start,visit):
    for e,w in trees[start]:
        if visit[e] == 0:
            visit[e] = visit[start] + w
            dfs(e,visit)

visit1 = [0]*(n+1)
dfs(1,visit1)
visit1[1] = 0

maxi = 0
index = 0
for i in range(len(visit1)):
    if maxi < visit1[i]:
        maxi = visit1[i]
        index = i
    
visit2 = [0]*(n+1)
dfs(index,visit2)
visit2[index] = 0
print(max(visit2))