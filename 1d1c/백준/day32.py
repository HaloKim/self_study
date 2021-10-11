# 11727 문제에 모듈러란걸 안보고내서 한번틀림 ..
'''
n = int(input())
dp = [0,1,3]
# for i in range(2,n+1):
#     dp[i] = i//2
#     tmp = 0
#     cnt = i-1
#     while(cnt):
#         tmp += dp[cnt]
#         cnt -= 1
#     dp[i] += tmp
# print((dp[-1]*2 + 1)% 10007)
for i in range(3,n+1):
    dp.append(dp[i-1] + dp[i-2]*2)
print(dp[-1]% 10007)
'''
# 1699 이해안감
import math
n = int(input())
dp = [0]*(n+1)
for i in range(1,n+1):
    dp[i] = i
    for j in range(1, int(math.sqrt(i))+1):
        dp[i] = min(dp[i], dp[i - j*j]+1)
print(dp[-1])