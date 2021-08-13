# 4641
'''
data = []
while (True):
    data.append(input().split())
    if data[-1][0] == '-1':
        data.pop()
        break
for i in range(len(data)):
    count = 0
    for k in data[i]:
            for m in data[i]:
                if k == m:
                    continue
                if int(k)*2 == int(m):
                    count += 1
    print(count)
'''

# 14501 모르겠다
n = int(input())
day = []
cost = []
dp=[]

for i in range(n):
  x,y = map(int, input().split())
  day.append(x)
  cost.append(y)
  dp.append(y)
dp.append(0)  #뒤에 0을 추가해서 인덱스초과 오류 방지

#뒤에서부터 확인
for i in range(n-1, -1, -1):
  if day[i] + i > n: #데드라인이 기한을 넘어가는경우
    dp[i] = dp[i+1]
  else:
    dp[i] = max(dp[i+1], cost[i]+dp[i+day[i]])

print(dp[0])