# 더 맵게.py
import heapq

def solution(scoville, K):
    heap = []
    cnt = 0
    for i in scoville:
        heapq.heappush(heap, i)
    while True:
        if heap[0] < K and len(heap) >= 2:
            a,b = heapq.heappop(heap), heapq.heappop(heap)
            heapq.heappush(heap, a+(b*2))
            cnt += 1
        elif heap[0] < K and len(heap) == 1:
            return -1
        else:
            return cnt