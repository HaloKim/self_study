# 피로도.py
from collections import deque

def solution(k, dungeons):
    cnt = 0
    q = deque()
    q.append([k,[]])
    while q:
        v, visit = q.popleft()
        for i in range(len(dungeons)):
            if i not in visit and v >= dungeons[i][0] and v - dungeons[i][1] >= 0:
                q.append([v - dungeons[i][1], visit+[i]])
            else:
                cnt = max(cnt, len(visit))
    return cnt