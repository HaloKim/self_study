# 체육복.py
def solution(n, lost, reserve):
    arr = [1]*(n+1)
    arr[0] = 0
    for i in lost:
        arr[i] -= 1
    for i in reserve:
        arr[i] += 1
    for i in range(1,len(arr)):
        if i == 1:
            if arr[i] == 0 and arr[i+1] > 1:
                arr[i] += 1
                arr[i+1] -= 1
        if i == len(arr)-1:
            if arr[i] == 0 and arr[i-1] > 1:
                arr[i] += 1
                arr[i-1] -= 1
        else:
            if arr[i] == 0 and arr[i-1] > 1:
                arr[i] += 1
                arr[i-1] -= 1
            elif arr[i] == 0 and arr[i+1] > 1:
                arr[i] += 1
                arr[i+1] -= 1
    ans = 0
    for i in arr:
        if i > 0:
            ans += 1
    return ans