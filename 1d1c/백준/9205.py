from collections import deque

t = int(input())

def bfs():
    q = deque()
    q.append([coor[0][0],coor[0][1]])
    visit[0] = 1
    while q:
        x,y = q.popleft()
        for i in range(1, len(coor)):
            a,b = coor[i]
            if abs(x-a) + abs(y-b) <= 1000 and visit[i] == 0:
                if i == len(coor)-1:
                    return 1
                visit[i] = 1
                q.append([a,b])
    return 0


for _ in range(t):
    n = int(input()) # 맥주를파는 편의점개수
    coor = [list(map(int, input().split())) for _ in range(n+2)]
    visit = [0]*len(coor)
    check = 0
    for i in range(len(coor)-1):
        a,b = coor[i]
        if bfs():
            check = 1
            break
    if check:
        print('happy')
    else:
        print('sad')


'''
3
0
1000 1000
1000 1001
1
0 0
1000 0
0 2000
2
0 0
10000 0
0 1000
0 2000
happy
sad
happy
'''