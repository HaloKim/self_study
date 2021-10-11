# 2839 최소공배수를 생각했어야함
n = int(input())
count = 0
while(True):
    if n == 0:
        break
    if n >= 15:
        n = n - 5
        count += 1
    elif n%5 == 0 and n >= 5:
        count += n//5
        n = n - (n//5)*5
    elif n%3 == 0:
        count += n//3
        n = n - (n//3)*3
    elif n >= 3:
        n = n - 3
        count += 1
    else:
        count = -1
        break
print(count)