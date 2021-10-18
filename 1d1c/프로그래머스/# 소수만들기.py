# 소수만들기.py
from itertools import combinations

def isPrime(n,cnt):
    if n < 2:
        return
    for i in range(2,n):
        if n % i == 0:
            return
    return 1

def solution(nums):
    cnt = 0
    for a,b,c, in combinations(nums,3):
        i = isPrime((a+b+c), cnt)
        if i == 1:
            cnt += i
    return cnt