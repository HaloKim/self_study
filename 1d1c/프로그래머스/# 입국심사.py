# 입국심사.py
def solution(n, times):
    time = 0
    left, right = 1, max(times)*n
    while left < right:
        mid = (left+right)//2
        total = 0
        for t in times:
            total += mid // t
        if total >= n:
            right = mid
        else:
            left = mid + 1
    time = left 
    return time