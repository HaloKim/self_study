# 최소직사각형.py
def solution(sizes):
    x,y = 0, 0
    for a,b in sizes:
        if b > a:
            y = max(y, a)
        else:
            y = max(y, b)
        x = max(x, a, b)
    print(x,y)
    return x*y
