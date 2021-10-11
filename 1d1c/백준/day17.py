# 11047
'''
n,k = map(int,input().split())
arr = []
count = 0
for _ in range(n):
    arr.append(int(input()))
arr.sort(reverse=True)
for i in range(n):
    if k == 0:
        break
    if k >= arr[i]:
        temp = k//arr[i]
        k = k - (temp * arr[i])
        count = count + temp
print(count)
'''

# 11054 LIS 알고리즘 
n = int(input())
arr = list(map(int,input().split()))
dpl = [0]*n
dpr = [0]*n

for i in range(0,n):
    dpl[i] = 1
    for j in range(0,i):
        if(arr[i] > arr[j]):
            dpl[i] = max(dpl[i], dpl[j]+1)

for i in range(n-1,-1,-1):
    dpr[i] = 1
    for j in range(n-1,i,-1):
        if(arr[i] > arr[j]):
            dpr[i] = max(dpr[i], dpr[j]+1)
result = [dpr[i] + dpl[i] for i in range(n)]
print(max(result)-1)