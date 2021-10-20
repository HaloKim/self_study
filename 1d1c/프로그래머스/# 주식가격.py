# 주식가격.py
from collections import deque

def solution(prices):
    prices = deque(prices)
    ans = deque()
    
    while prices:
        p = prices.popleft()
        cnt = 0
        for i in prices:
            cnt += 1
            if p > i:
                break
        ans.append(cnt)
    return list(ans)