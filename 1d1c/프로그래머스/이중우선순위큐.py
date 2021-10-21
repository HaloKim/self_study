# 이중우선순위큐.py
import heapq

def solution(operations):
    heap = []
    for i in operations:
        o,v = i.split()
        v = int(v)
        if o == 'I':
            heapq.heappush(heap, v)
        elif o == 'D':
            if len(heap) > 0:
                if v == 1:
                    heap.pop(heap.index(heapq.nlargest(1,heap)[0]))
                else:
                    heapq.heappop(heap)
    if len(heap) == 0:
        return [0,0]
    else:
        return [heapq.nlargest(1,heap)[0], heapq.nsmallest(1,heap)[0]]