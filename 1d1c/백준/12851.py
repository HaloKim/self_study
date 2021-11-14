from collections import deque

a,b = map(int,input().split())
visit = [0]*(int(1e5)+1)

cnt = 0
def bfs():
    global cnt
    q = deque()
    q.append(a)
    visit[a] = 1
    while q:
        x = q.popleft()
        if x == b:
            cnt += 1
        for i in (x*2),(x-1),(x+1):
            if 0 <= i <= len(visit)-1:
                if visit[i] == 0 or visit[i] == visit[x]+1:
                    visit[i] = visit[x] + 1
                    q.append(i)
bfs()
print(visit[b]-1)
print(cnt)