import sys
sys.setrecursionlimit(int(1e9))
def solution(n, k):
    global cnt
    cnt = 0
    dfs([],n,k)
    return 
n = 3
k = 5
visit = [0]*(n+1)
ans = []
def dfs(arr, n, k):
    global cnt
    if len(arr) == n:
        cnt += 1
        if cnt == k:
            print(arr)
            return
    for i in range(1,n+1):
        if visit[i] == 0:
            arr.append(i)
            visit[i] = 1
            dfs(arr,n,k)
            arr.pop()
            visit[i] = 0

solution(n,k)