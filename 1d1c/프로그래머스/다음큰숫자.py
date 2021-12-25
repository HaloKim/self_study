def solution(n):
    check = bin(n).count('1')
    while True:
        n += 1
        if bin(n).count('1') == check:
            return n