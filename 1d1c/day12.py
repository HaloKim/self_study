# 4811 어렵다
arr = []
def pill(n, arr):
    arr = [[0]*(n+1) for _ in range(n+1)]
    for i in range(n+1):
        for j in range(1,n+1):
            if i == 0:
                arr[i][j] = 1
            elif i <= j:
                arr[i][j] = arr[i-1][j] + arr[i][j-1]
    print(max(arr[-1]))
while(True):
    n = int(input())
    if n == 0:
        break
    pill(n, arr)
    