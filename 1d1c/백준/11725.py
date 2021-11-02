import sys
from sys import stdin
input = stdin.readline
sys.setrecursionlimit(int(1e9))

n = int(input())
trees = [[] for _ in range(n+1)]
parents = [0]*(n+1)
for _ in range(n-1):
    a,b = map(int, input().split())
    trees[a].append(b)
    trees[b].append(a)

def dfs(start):
    for i in trees[start]:
        if parents[i] == 0:
            parents[i] = start
            dfs(i)
dfs(1)
for i in range(2,n+1):
    print(parents[i])