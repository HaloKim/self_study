# 12865re.py
n,k = map(int,input().split())
w,v = [0],[0]
dp = [[0]*(k+1) for _ in range(n+1)]
for i in range(n):
    a,b = map(int,input().split())
    w.append(a)
    v.append(b)

for i in range(1, n+1):
    for j in range(1, k+1): # 현재 가방의 크기
        if j >= w[i]:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i]]+v[i])
        else:
            dp[i][j] = dp[i-1][j]
print(dp[n][k])