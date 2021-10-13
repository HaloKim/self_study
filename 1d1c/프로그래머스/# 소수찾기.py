# 소수찾기
from itertools import permutations

def isprime(v):
    if v < 2:
        return 0
    for i in range(2,v):
        if v % i == 0:
            return 0
    return 1

def solution(numbers):
    answer = 0
    numbers = list(numbers)
    temp = []
    for i in range(1,len(numbers)+1):
        temp += map(int, list(map(''.join, permutations(numbers,i))))
    temp = set(temp)
    for i in temp:
        if isprime(i):
            answer += 1
    return answer