# 11053
'''
n = int(input())
arr = list(map(int, input().split()))
lis = [0]*n
for i in range(n):
    lis[i] = 1
    for j in range(n):
        if arr[i] > arr[j]:
            lis[i] = max(lis[i], lis[j]+1)
print(max(lis))
'''
# 11048
n,m = map(int,input().split())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
dp = [[0]*(m) for _ in range(n)]
dp[0][0] = arr[0][0]
for i in range(n):
    for j in range(m):
        if i == 0 and j == 0:
            continue
        elif i == 0:
            dp[i][j] = arr[i][j] + dp[i][j-1]
        elif j > 0:
            dp[i][j] = max(arr[i][j] + dp[i][j-1], arr[i][j] + dp[i-1][j])
        elif j == 0:
            dp[i][j] = arr[i][j] + dp[i-1][j]
print(dp[-1][-1])