from sys import stdin
input = stdin.readline

n = int(input())
dp = [n]
cnt = 0
def temp(dp):
    global cnt
    cnt += 1
    tmp = []
    for i in dp:
        if i % 3 == 0 and i >= 3:
            tmp.append(i//3)
        if i % 2 == 0 and i >= 2:
            tmp.append(i//2)
        tmp.append(i-1)
    return tmp

while True:
    if min(dp) == 1:
        print(cnt)
        exit()
    dp = temp(dp)