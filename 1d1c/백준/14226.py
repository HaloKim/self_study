from collections import deque
from sys import stdin
input = stdin.readline

S = int(input().strip())
visit = [[0]*1001 for _ in range(1001)]
def bfs():
    q = deque()
    q.append(([1], [], 1))
    visit[1][0] = 1
    while q:
        v, clip, now = q.popleft()
        lv = len(v)
        lc = len(clip)
        if len(v) == S:
            print(now-1)
            return
        if 0 <= lv <= 1000:
            if visit[lv][lv] == 0:
                q.append((v,v,now+1))
                visit[lv][lv] = 1
        if 0 <= lc <= 1000 and 0 <= lv+lc <= 1000:
            if visit[lv+lc][lc] == 0 and clip:
                q.append((v+clip,clip,now+1))
                visit[lv+lc][lc] = 1
        if 0 <= lv-1 <= 1000 and 0 <= lc <= 1000:
            if visit[lv-1][lc] == 0:
                q.append((v[:-1],clip,now+1))
                visit[lv-1][lc] = 1
bfs()