from sys import stdin
input = stdin.readline

R, C = map(int, input().split())
board = [input().strip() for _ in range(R)]
move = [[-1,0],[0,1],[0,-1],[1,0]]

maxi = 1
def bfs():
    global maxi
    q = set([(0, 0, board[0][0])])
    while q:
        x,y,arr = q.pop()
        for a,b in move:
            dx = x + a
            dy = y + b
            if 0 <= dx < R and 0 <= dy < C:
                if board[dx][dy] not in arr:
                    q.add((dx,dy,arr+board[dx][dy]))
                    maxi = max(len(arr)+1, maxi)

bfs()
print(maxi)