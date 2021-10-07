# 14499
N,M,x,y,k = map(int,input().split())
mapp = [list(map(int,input().split())) for _ in range(N)]
order = list(map(int,input().split()))
dice = [0]*6
d = ((1,0),(0,1),(0,-1),(-1,0))

def change(w):
    if w == 1:
        dice[0],dice[2],dice[4],dice[5] = dice[5],dice[4],dice[0],dice[2]
    if w == 2:
        dice[0],dice[2],dice[4],dice[5] = dice[4],dice[5],dice[2],dice[0]
    if w == 3:
        dice[0],dice[1],dice[2],dice[3] = dice[3],dice[0],dice[1],dice[2]
    if w == 4:
        dice[0],dice[1],dice[2],dice[3] = dice[1],dice[2],dice[3],dice[0]

for w in range(k):
    dx,dy = d[order[w]%4]
    nx = x + dx
    ny = y + dy
    if not 0 <= nx < N or not 0 <= ny < M:
        continue
    change(order[w])
    if mapp[nx][ny] == 0:
        mapp[nx][ny] = dice[0]
    else:
        dice[0] = mapp[nx][ny]
        mapp[nx][ny] = 0
    print(dice[2])
    x,y = nx,ny