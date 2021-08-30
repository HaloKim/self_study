# 9095 깔끔한 코드로 바꿈
'''
n = int(input())
line = []
for _ in range(n):
    line.append(int(input()))

for n in line:
    dp = [1,2,4]
    if n >= 3:
        for i in range(3,n+1):
            dp.append(dp[i-3] + dp[i-2] + dp[i-1])
        print(dp[n-1])
    else:
        print(dp[n-1])
'''
t = int(input())
def func(x):
    if x == 1:
        return 1
    if x == 2:
        return 2
    if x == 3:
        return 4
    else:
        return func(x-3) + func(x-2) + func(x-1)
for i in range(t):
    n = int(input())
    print(func(n))