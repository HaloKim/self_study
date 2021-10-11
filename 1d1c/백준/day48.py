# 1789
# import sys

# n = int(sys.stdin.readline().strip())

# cnt = 1
# total = 0
# while(True):
#     if total > n:
#         break
#     total += cnt
#     cnt += 1

# cnt -= 1

# while(True):
#     if n-total > cnt:
#         print(cnt + 1)
#         break
#     total -= cnt
#     cnt -= 1

# 13305
# import sys

# n = int(sys.stdin.readline().strip())
# road = list(map(int, sys.stdin.readline().strip().split()))
# price = list(map(int, sys.stdin.readline().strip().split()))
# price.pop()
# mini = price[0]
# sum = 0
# for i in range(n-1):
#     if mini > price[i]:
#         mini = price[i]
#     sum += (mini * road[i])
# print(sum)

# 1339
# import sys

# n = int(sys.stdin.readline().strip())
# arr = []
# for _ in range(n):
#     arr.append(list(sys.stdin.readline().strip()))
# dic = {}
# for i in range(n):
#     for j in range(len(arr[i])):
#         if arr[i][j] in dic:
#             dic[arr[i][j]] += 10**(len(arr[i])-j-1)
#         else:
#             dic[arr[i][j]] = 10**(len(arr[i])-j-1)
# val = []
# for i in dic.values():
#     val.append(i)
# val.sort(reverse=True)
# cnt = 9
# total = 0
# for i in val:
#     total += (i*cnt)
#     cnt -= 1
# print(total)