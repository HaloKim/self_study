# 11401 페르마, 
# import sys

# sys.setrecursionlimit(10**6)
# n,k = map(int,input().split())
# p = 1000000007

# fact = [1 for _ in range(n+1)]

# for i in range(2,n+1):
#     fact[i] = fact[i-1] * i % p

# def power(a, b):
#     if b == 0:
#         return 1
#     if b % 2:   #홀수이면
#         return (power(a, b//2) ** 2 * a) % p
#     else:
#         return (power(a, b//2) ** 2) % p

# A = fact[n]
# B = (fact[n-k] * fact[k]) % p

# print(A%p * (power(B, p-2)%p)%p)

