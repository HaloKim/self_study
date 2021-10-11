#7568
N = int(input())
info = {}
arr = [1]*N
for i in range(N):
    t1, t2 = input().split()
    info.update({i : [int(t1), int(t2)]})
for i in range(N):
    for j in range(i+1, N):
        if info[i][0] > info[j][0] and info[i][1] > info[j][1]:
            arr[j] += 1
        if info[i][0] < info[j][0] and info[i][1] < info[j][1]:
            arr[i] += 1
for i in arr:
    print(i, end=' ')

