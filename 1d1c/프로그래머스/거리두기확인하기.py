from collections import deque
def solution(places):
    ans = []
    for place in places:
        flag = 0
        for j in range(5):
            for k in range(5):
                if place[j][k] == 'P':
                    if bfs(place, j, k) == 0:
                        flag = 1
                        break
            if flag:
                break
        if flag:
            ans.append(0)
        else:
            ans.append(1)
    return ans

def bfs(arr, x, y):
    q = deque()
    q.append([x,y,0])
    visit = [[0]*5 for _ in range(5)]
    visit[x][y] = 1
    while q:
        x,y,v = q.popleft()
        if arr[x][y] == 'P' and 1 <= v <= 2:
            return 0
        if v > 2:
            break
        for a,b in (1,0),(-1,0),(0,1),(0,-1):
            dx = x + a
            dy = y + b
            if 0 <= dx < 5 and 0 <= dy < 5 and visit[dx][dy] == 0:
                if arr[dx][dy] != 'X':
                    visit[dx][dy] = 1
                    q.append([dx,dy,v+1])
    return