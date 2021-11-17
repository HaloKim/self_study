N,M = map(int, input().split())
arr = list(map(int,input().split()))
arr.sort()
maxi = 0
for i in range(N-2):
    for j in range(i+1,N-1):
        for l in range(j+1,N):
            temp = arr[i] + arr[j] + arr[l]
            if temp <= M:
                maxi = max(maxi, temp)
print(maxi)