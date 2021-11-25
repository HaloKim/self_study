from math import gcd
def solution(w,h):
    ori = w*h
    return ori-(w+h-gcd(w,h))