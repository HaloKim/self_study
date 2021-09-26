# # 15650
# from collections import deque

# n,m = map(int, input().split())
# visit = [0]*(n+1)
# q = deque()
# def dfs(start):
#     if len(q) == m:
#         print(*q)
#         return
#     for i in range(start,n+1):
#         if visit[i] == 0:
#             visit[i] = 1
#             q.append(i)
#             dfs(i+1)
#             q.pop()
#             visit[i] = 0
#     return
# dfs(1)

# # 15651
# from collections import deque

# n,m = map(int, input().split())
# q = deque()
# visit = [0]*(n+1)

# def dfs(start):
#     if len(q) == m:
#         print(*q)
#         return
#     for i in range(start, n+1):
#         if visit[i] < m:
#             visit[i] += 1
#             q.append(i)
#             dfs(1)
#             q.pop()
#             visit[i] -= 1
#     return
# dfs(1)

# # 15652
# from collections import deque

# n,m = map(int, input().split())
# q = deque()
# visit = [0]*(n+1)

# def dfs(start):
#     if len(q) == m:
#         print(*q)
#         return
#     for i in range(start, n+1):
#         if visit[i] < m:
#             visit[i] += 1
#             q.append(i)
#             dfs(i)
#             q.pop()
#             visit[i] -= 1
#     return
# dfs(1)

# 9663
n = int(input())

