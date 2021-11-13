from collections import deque

N, K = map(int, input().split())
if N == K:
    print(0)
    exit()
visit = [0]*(10**5+1)
def bfs(N,s):
    q = deque()
    q.append([N,s])
    visit[N] = 1
    while q:
        n,s = q.popleft()
        if n == K:
            print(s)
            return
        for i in (n*2,n-1,n+1):
            if 0 <= i <= int(10**5):
                if visit[i] == 0:
                    if i == n*2:
                        visit[i] = 1
                        q.append([i,s])
                    else:
                        visit[i] = 1
                        q.append([i,s+1])
bfs(N,0)