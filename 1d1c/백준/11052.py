N = int(input())
dp = [0]*(N+1)
P = [0] + list(map(int, input().split()))
dp[1] = P[1]
for i in range(2, N+1):
    for j in range(1, i+1):
        if dp[i] < dp[i-j] + P[j]:
            dp[i] = dp[i-j] + P[j]
print(dp[N])