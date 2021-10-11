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

# 9663 시간초과
# import sys
# from collections import deque
# n = int(sys.stdin.readline())
# qeen = deque()
# qeen = [0]*n

# def dfs(qeen, row):
#     cnt = 0
#     if n == row:
#         return 1
#     for col in range(n):
#         qeen[row] = col
#         for i in range(row):
#             if qeen[i] == qeen[row]:
#                 break
#             if abs(qeen[i]-qeen[row]) == row - i:
#                 break
#         else:
#             cnt += dfs(qeen, row+1)
#     return cnt

# print(dfs(qeen, 0))

# 최적화를 적용한 코드
n = int(input())
row_check = [False] * n
left = [False] * (2*n-1)
right = [False] * (2*n-1)
cnt = 0

def queen(qn):
    global n, cnt
    if qn == n:
        cnt += 1
        return
    else:
        for j in range(n):
            if not row_check[j] and not left[j + qn] and not right[n-1 + qn - j]:
                row_check[j] = left[j + qn] = right[n-1 + qn - j] = True
                queen(qn + 1)
                row_check[j] = left[j + qn] = right[n-1 + qn - j] = False

queen(0)
print(cnt)