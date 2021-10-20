# 프린터.py
def solution(priorities, location):
    answer = 0
    cnt = 0
    while priorities:
        maxi = max(priorities)
        if cnt == len(priorities):
            cnt = 0
            continue
        elif priorities[cnt] == maxi and cnt == location:
            answer += 1
            return answer
        elif priorities[cnt] == maxi:
            priorities[cnt] = -1
            answer += 1
        cnt += 1
    return answer