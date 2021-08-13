# 4641
'''
data = []
while (True):
    data.append(input().split())
    if data[-1][0] == '-1':
        data.pop()
        break
for i in range(len(data)):
    count = 0
    for k in data[i]:
            for m in data[i]:
                if k == m:
                    continue
                if int(k)*2 == int(m):
                    count += 1
    print(count)
'''

# 14501 모르겠다
day = int(input())
money = []
next = 0
total = 0
start = 0
maximum = []
for _ in range(day):
    money.append(input().split())
def temp(money, start, total, maximum):
    next = start
    next += int(money[start][0])
    if next >= day:
        maximum.append(total)
        print(maximum)
        return
    total += int(money[start][1])
    print(money[start])
    temp(money, next, total, maximum)

for i in range(day):
    print(i)
    temp(money, i, total, maximum)
print(max(maximum))