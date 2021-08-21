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
