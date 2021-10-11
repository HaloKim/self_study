from collections import deque

def solution(numbers, target):
    ans = 0
    q = deque()
    q.append([0,0])
    while q:
        v,i = q.popleft()
        if i == len(numbers):
            if v == target:
                ans += 1
        else:
            n = numbers[i]
            q.append([v+n, i+1])
            q.append([v-n, i+1])
    return ans