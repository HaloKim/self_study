# 2565 뭐가문제인지모르겠다
'''
n = int(input())
temp = []
for i in range(n):
    temp.append(list(map(int,input().split())))
count = 1
tmp = 0
temp.sort()
while(True):
    maximum = []
    for i in range(len(temp)):
        count = 0
        for j in range(len(temp)):
            if i == j:
                continue
            if temp[i][0] > temp[j][0] and temp[i][1] < temp[j][1]:
                count += 1
            if temp[i][0] < temp[j][0] and temp[i][1] > temp[j][1]:
                count += 1
        maximum.append(count)
    if max(maximum) == 0:
        break
    temp.pop(maximum.index(max(maximum)))
    tmp += 1
print(tmp)
'''

n = int(input())
temp = []
for i in range(n):
    temp.append(list(map(int,input().split())))
temp.sort()
lis = [0]*n
for i in range(n):
    lis[i] = 1
    for j in range(i):
        if temp[i][1] > temp[j][1]:
            lis[i] = max(lis[i], lis[j]+1)
print(lis)
print(n-max(lis))