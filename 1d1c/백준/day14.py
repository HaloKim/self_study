'''
# 10844 설계실패
n = int(input())
dp = [[0]*(10) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(10):
        if i == 1 and j > 0:
            dp[i][j] = 1
        elif j==9:
            dp[i][j] = dp[i-1][j-1]
        elif j==0:
            dp[i][j] = dp[i-1][j+1]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
print(sum(dp[-1]) % 1000000000)
'''
'''
# 첫시도 알고리즘자체가 틀렸나보다. 후반에 틀림
n = int(input())
dp = [[0]*(10) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,10):
        if i == 1:
            dp[i][j] = j
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
print(max(dp[-1]) % 1000000000 )
'''
