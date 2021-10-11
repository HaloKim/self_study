# 11399
'''
people = int(input())
times = []
times = input().split()
for i in range(len(times)):
    times[i] = int(times[i])
change = 0
total = 0
temp = []
for i in range(people):
    total += (min(times))
    temp.append(total)
    times.remove(min(times))
print(sum(temp))
'''

# 1439
'''
data = input()
temp = []
for i in range(len(data)):
    if i == 0:
        temp.append(data[i])
    if i != 0:
        if data[i-1] != data[i]:
            temp.append(data[i])
if temp.count('0') > temp.count('1'):
    print(temp.count('1'))
else:
    print(temp.count('0'))
'''
