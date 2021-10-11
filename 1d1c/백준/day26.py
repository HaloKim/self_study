# 2565 틀림
'''
n = int(input())
temp = []
for i in range(n):
    temp.append(list(map(int,input().split())))
temp.sort()
tmp = 0
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
    print(temp)
    tmp += 1
print(tmp)
'''
# 정확한 답
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

'''
10
1 6
2 8
3 2
4 9
5 5
6 10
7 4
8 1
9 7
10 3

5
1 3
2 1
3 5
4 2
5 4
'''