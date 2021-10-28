from collections import deque

N,M = map(int, input().split())
ladder = dict()
snake = dict()
ans = [0]*101
visit = [0]*101
for _ in range(N):
    s,e = map(int, input().split())
    ladder[s] = e
for _ in range(M):
    s,e = map(int, input().split())
    snake[s] = e

def bfs():
    q = deque([1])
    visit[1] = 1
    while q:
        now = q.popleft()
        for i in range(1,7):
            move = now + i
            if 0 < move <= 100 and visit[move] == 0:
                if move in ladder.keys():
                    move = ladder[move]
                
                if move in snake.keys():
                    move = snake[move]

                if visit[move] == 0:
                    q.append(move)
                    visit[move] = 1
                    ans[move] = ans[now] + 1
    return

bfs()
print(ans[-1])