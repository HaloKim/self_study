from sys import stdin
input = stdin.readline

n = int(input())
arr = list(map(int, input().split()))
maxi = [arr[0]]
for i in range(len(arr)-1):
    maxi.append(max(maxi[i]+arr[i+1], arr[i+1]))
print(max(maxi))