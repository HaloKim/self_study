from math import factorial
# def solution(n, k):
#     ans = []
#     arr = list(range(1,n+1))
#     while n != 0:
#         facto = factorial(n-1)
#         ans.append(arr.pop((k-1)//facto))
#         n,k = n-1, k%facto
#     return ans

def solution(n,k):
    ans = []
    arr = [i+1 for i in range(n)]
    while n != 0:
        facto = factorial(n-1)
        ans.append(arr.pop((k-1)//facto))
        n,k = n-1, k%facto
    print(ans)
solution(3, 5)