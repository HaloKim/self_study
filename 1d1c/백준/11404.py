import sys
input = sys.stdin.readline
INF = int(1e9)

N = int(input())
M = int(input())
bus = [[INF]*N for _ in range(N)]
for i in range(M):
    a,b,c = map(int, input().strip().split())
    if bus[a-1][b-1] > c:
        bus[a-1][b-1] = c
for k in range(N):
    for i in range(N):
        for j in range(N):
            if i != j and bus[i][j] > bus[i][k] + bus[k][j]:
                bus[i][j] = bus[i][k] + bus[k][j]
for i in range(N):
    for j in bus[i]:
        if j == INF:
            j = 0
        print(j, end=' ')
    print()