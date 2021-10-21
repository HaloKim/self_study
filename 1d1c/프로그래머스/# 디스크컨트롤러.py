# 디스크컨트롤러.py
import heapq

def solution(jobs):
    ans = []
    heap = []
    time = 0
    jobs.sort()
    l = len(jobs)
    cnt = 0
    while cnt != l:
        while len(jobs):
            if jobs[0][0] <= time:
                s,ms = jobs.pop(0)
                heapq.heappush(heap, [ms,s])
            else:
                break
        if heap:
            ms, s = heapq.heappop(heap)
            time += ms
            ans.append(time - s)
            cnt += 1
        else:
            time += 1
    return sum(ans)//cnt