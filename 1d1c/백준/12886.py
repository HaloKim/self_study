from collections import deque
from sys import stdin
input = stdin.readline

A,B,C = map(int,input().split())

def bfs():
    q = deque()
    q.append([A,B,C])
    visit[A][B] = 1

    while q:
        a, b, c = q.popleft()
        if a == b and b == c and c == a:
            return 1
        if a > b and not visit[a - b][2 * b]:
            visit[a - b][2 * b] = 1
            q.append((a - b, 2 * b, c))
        if a < b and not visit[2 * a][b - a]:
            visit[2 * a][b - a] = 1
            q.append((2 * a, b - a, c))
        if b > c and not visit[b - c][2 * c]:
            visit[b - c][2 * c] = 1
            q.append((a, b - c, 2 * c))
        if b < c and not visit[2 * b][c - b]:
            visit[2 * b][c - b] = 1
            q.append((a, 2 * b, c - b))
        if c > a and not visit[2 * a][c - a]:
            visit[2 * a][c - a] = 1
            q.append((2 * a, b, c - a))
        if c < a and not visit[a - c][2 * c]:
            visit[a - c][2 * c] = 1
            q.append((a - c, b, 2 * c))
    return 0

total = A+B+C
visit = [[0]*1500 for _ in range(1500)]
print(bfs())