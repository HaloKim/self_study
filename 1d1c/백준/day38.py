# 10872
'''
import sys

n = int(sys.stdin.readline())
tmp = 1
for i in range(1,n+1):
    tmp *= i
print(tmp)
'''
# 10870
'''
import sys
n = int(sys.stdin.readline())
def fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
print(fibo(n))
'''
# 11728
import sys
n = int(sys.stdin.readline())
def func(n,a,b,c):
    if n == 1:
        print(a,c)
    else:
        func(n-1,a,c,b)
        print(a,c)
        func(n-1,b,a,c)
total = 1
for i in range(n-1):
    total = total*2 + 1
print(total)
func(n,1,2,3)