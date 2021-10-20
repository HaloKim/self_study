# 기능개발.py
def solution(progresses, speeds):
    time = 0
    cnt = 0
    ans = []
    while progresses:
        if progresses[0] + speeds[0]*time >= 100:
            progresses.pop(0)
            speeds.pop(0)
            cnt += 1
        else:
            if cnt > 0:
                ans.append(cnt)
                cnt = 0
            time += 1
    ans.append(cnt)
    return ans