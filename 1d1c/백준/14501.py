from sys import stdin
input = stdin.readline

N = int(input())
dp = [0]*(N+1)
arr = [list(map(int,input().strip().split())) for _ in range(N)]
# for i in range(N):
#     if arr[i][0] <= N - i:
#         dp[i + arr[i][0]] = max(dp[arr[i][0] + i], dp[i]+arr[i][1])
#     dp[i+1] = max(dp[i+1], dp[i])
# print(dp[N])
for i in range(N-1,-1,-1):
    if i + arr[i][0] > N:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], arr[i][1] + dp[i + arr[i][0]])
print(dp[0])