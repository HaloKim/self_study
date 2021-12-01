def solution(land):
    dp = [[0]*4 for _ in range(len(land))]
    dp[0] = land[0]
    for i in range(1,len(land)):
        for j in range(4):
            dp[i][j] = max(list(dp[i-1][0:j] + dp[i-1][j+1:])) + land[i][j]
    return max(dp[-1])