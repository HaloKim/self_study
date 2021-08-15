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
times = []
for _ in range(n):
  times.append(list(map(int,input().split())))
print(times)
dp = [0] * n

for i in range(n):
	if i + times[i][0] <= n:
		dp[i] = times[i][1]
		for j in range(i):
			if j + times[j][0] <= i:
				dp[i] = max(dp[i], dp[j] + times[i][1])
print(max(dp))
