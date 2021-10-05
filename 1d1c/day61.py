# 1080
n,m = map(int,input().split())

a = [list(map(int,input())) for _ in range(n)]
b = [list(map(int,input())) for _ in range(n)]

cnt = 0
def check(i,j,a):
    for w in range(i,i+3):
            for k in range(j,j+3):
                a[w][k] = 1 - a[w][k]

for i in range(n-2):
    for j in range(m-2):
        if a[i][j] != b[i][j]:
            check(i,j,a)
            cnt += 1

if a == b:
    print(cnt)
else:
    print(-1)