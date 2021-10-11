# 1026
# n = int(input())
# A = list(map(int,input().split()))
# B = list(map(int,input().split()))
# A.sort()
# B.sort(reverse=True)
# mini = n*100
# total = 0
# for i in range(n):
#     total = total + A[i]*B[i]
# print(total)

# 1744 은근 어려웠음
n = int(input())
seq = []

for _ in range(n):
    seq.append(int(input()))

seq.sort()
mini = []
plus = []

for i in seq:
    if i < 1:
        mini.append(i)
    else:
        plus.append(i)

ans = []
while len(mini) > 1:
    a = mini.pop(0)
    b = mini.pop(0)
    if a*b > a+b:
        ans.append(a*b)
    else:
        ans.append(a+b)

while len(plus) > 1:
    b = plus.pop()
    a = plus.pop()
    if a*b > a+b:
        ans.append(a*b)
    else:
        ans.append(a+b)
ans = ans + mini + plus
print(sum(ans))