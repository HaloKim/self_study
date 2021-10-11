# 1197
'''
n,m = map(int,input().split())
cycle_table = [i for i in range(n+1)]
arr = []
for i in range(m):
    arr.append(list(map(int,input().split())))
arr.sort(key=lambda x:x[-1])

def find(x):
    if cycle_table[x] != x:
        return find(cycle_table[x])
    return cycle_table[x]

def union(a,b):
    x = find(a)
    y = find(b)
    if x < y:
        cycle_table[y] = x
    else:
        cycle_table[x] = y

mst = 0
for i in range(m):
    a,b,c = arr[i]
    if find(a) != find(b):
        mst += c
        union(a,b)
print(mst)
'''

'''
# 11055
n = int(input())
arr = []
arr = list(map(int,input().split()))
dp = [0]*(n)
for i in range(n):
    dp[i] = arr[i]
    for j in range(i):
        if arr[i] > arr[j] and dp[i] < dp[j] + arr[i]:
            dp[i] = dp[j] + arr[i]
print(max(dp))
'''
'''
# 11722
n = int(input())
arr = []
arr = list(map(int,input().split()))
dp = [0]*(n)
for i in range(n-1,-1,-1):
    dp[i] = 1
    for j in range(n-1,i-1,-1):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))
'''
# 14003 시간초과
import bisect
n = int(input())
record = [0] * n
arr = list(map(int,input().split()))
dp = [arr[0]]
record[0] = 1
for i in range(1, n):
    if dp[-1] < arr[i]:
        dp.append(arr[i])
        record[i] = len(dp)
    else:
        idx = bisect.bisect_left(dp, arr[i])
        dp[idx] = arr[i]
        record[i] = idx+1

lis = []
find_dp = len(dp)
for i in range(len(record)-1,-1,-1):
    if record[i] == find_dp:
        lis.append(arr[i])
        find_dp -= 1
    if find_dp < 1:
        break
print(len(lis))
print(*lis[::-1])