# 124 나라의 숫자.py
def solution(n):
    ans = ''
    while n > 0:
        n -= 1
        ans = '124'[n%3] + ans
        n = n//3
    return ans