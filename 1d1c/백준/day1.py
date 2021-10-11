'''
#10818
count = input()
temp = input().split()
temp = [int(i) for i in temp]
print(min(temp),max(temp))
'''

'''
#2562
tmp = []
for i in range(9):
    tmp.append(input())
arr = [int(i) for i in tmp]
i = arr.index(max(arr))
print(max(arr))
print(i+1)
'''
'''
#2577
a = int(input())
b = int(input())
c = int(input())
multi = a*b*c
tmp = str(multi)
for i in range(10):
    print(tmp.count(str(i)))
'''
'''
#1546
course = int(input())
arr = []
n_points = [0 for i in range(course)]
arr = input().split()
points = [int(i) for i in arr]
m = max(points)
for i in range(course):
    n_points[i] = (points[i]/m)*100
print(sum(n_points)/course)
'''
#4344
test = int(input())
result = []
for i in range(test):
    line_case = []
    point = []
    line_case = input().split()
    point = [int(i) for i in line_case]
    avg_point = sum(point[1:])/len(point[1:])
    up = 0
    for j in range(point[0]):
        if point[j+1] > avg_point:
            up += 1
    result.append(round((up/point[0])*100,3))
for i in result:
    print("%.3f%%" % i)
