T = int(input())
def fact(n):
    num = 1
    for i in range(1,n+1):
        num *= i
    return num

for _ in range(T):
    w,e = map(int, input().split())
    if w == e:
        print(1)
    else:
        print(fact(e)//(fact(e-w)*fact(w)))