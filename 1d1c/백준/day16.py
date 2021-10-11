# 1931 시간초과
'''
n = int(input())
arr = []
save = []
for _ in range(n):
    arr.append(list(map(int,input().split())))
arr = sorted(arr)

def temp(start):
    count = 0
    while(start+1 <= n):
        for i in range(start+1, n):
            if arr[i][0] >= arr[start][1]:
                start = i
                count += 1
        start += 1
    return count

start = 0
while(True):
    if start > n:
        break
    count = temp(start)
    save.append(count)
    start += 1
print(max(save)+1)
'''
n = int(input())
arr = []
save = []
for _ in range(n):
    arr.append(list(map(int,input().split())))

arr = sorted(arr)
arr = sorted(arr, key=lambda arr: arr[1])
# print(arr)
count = 0
j = 0
for i in range(1,n):
    if arr[i][0] >= arr[j][1]:
        # print(arr[i])
        j = i
        count += 1
print(count+1)