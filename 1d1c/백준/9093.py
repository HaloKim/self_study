from sys import stdin
input = stdin.readline
n = int(input())
for _ in range(n):
    words = input().strip().split()
    for i in words:
        if len(i) > 1:
            print(i[::-1], end=' ')
        else:
            print(i, end=' ')
    print()