N, L = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

cnt = 0
ans = 0
while True:
    if cnt >= len(arr):
        break
    tmp = arr[cnt] + L -1
    for i in range(cnt,len(arr)):
        if arr[i] <= tmp:
            cnt += 1
    ans += 1
print(ans)