# 4811re.py
ans = []
while True:
    c = int(input())
    if c == 0:
        break
    dp = [[0]*(c+1) for _ in range(c+1)]
      
    for i in range(c+1):
        for j in range(1,c+1):
            if i == 0:
                dp[0][j] = 1
            elif i <= j:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    print(dp[-1][-1])