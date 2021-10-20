# 도둑질.py
def solution(money):
    f = [0]*len(money)
    s = [0]*len(money)
    f[0] = money[0]
    for i in range(1,len(money)-1):
        f[i] = max(f[i-2] + money[i], f[i-1])
    for i in range(1,len(money)):
        s[i] = max(s[i-2] + money[i], s[i-1])
    return max(f[-2],s[-1])