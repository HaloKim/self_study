from sys import stdin
input = stdin.readline
N = int(input().strip())
w = list(map(int, input().strip().split()))
w.sort()
num = 1
for i in range(N):
    if num < w[i]:
        break
    num += w[i]
print(num)