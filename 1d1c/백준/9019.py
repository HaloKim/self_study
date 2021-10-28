from collections import deque
from sys import stdin
input = stdin.readline

T = int(input())

def bfs(A,B):
    q = deque()
    q.append([A,''])
    visit[A] = 1
    while q:
        v, ans = q.popleft()

        if v == B:
            return ans
        
        d = (v*2)%10000
        if visit[d] == 0:
            q.append([d, ans+'D'])
            visit[d] = 1

        s = (v-1)%10000
        if visit[s] == 0:
            q.append([s, ans+'S'])
            visit[s] = 1

        ln = int(v % 1000 * 10 + v / 1000)
        if visit[ln] == 0:
            q.append([ln, ans+'L'])
            visit[ln] = 1
        
        rn = int(v % 10 * 1000 + v // 10)
        if visit[rn] == 0:
            q.append([rn, ans+'R'])
            visit[rn] = 1
    return ans

for _ in range(T):
    A,B = map(int,input().split())
    visit = [0]*10000
    print(bfs(A,B))