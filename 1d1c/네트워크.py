from collections import deque

def bfs(i,visit,n,computers):
    q = deque()
    q.append(i)
    visit[i] = 1
    while q:
        i = q.popleft()
        for index,_ in enumerate(computers[i]):
            if visit[index] == 0 and computers[i][index] == 1:
                visit[index] = 1
                q.append(index)
    
def solution(n, computers):
    answer = 0
    visit = [0]*n
    for i in range(n):
        for j,_ in enumerate(computers[i]):
            if visit[j] == 0:
                bfs(j,visit,n,computers)
                answer += 1
    return answer