def solution(x):
    plus = []
    for i in str(x):
        plus.append(int(i))
    if x%sum(plus) == 0:
        return True
    return False
