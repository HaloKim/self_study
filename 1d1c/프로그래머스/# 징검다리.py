# 징검다리.py
def solution(distance, rocks, n):
    answer = 0
    start, end = 0, distance
    rocks.sort()

    while start <= end:
        mid = (start+end)//2
        dels = 0
        pres = 0
        for i in rocks:
            if i - pres < mid:
                dels += 1
            else:
                pres = i
            if dels > n:
                break
        if dels > n:
            end = mid - 1
        else:
            answer = mid
            start = mid + 1
    return answer