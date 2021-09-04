# 1922 크루스칼
n = int(input())
m = int(input())
arr = []
for i in range(m):
    arr.append(list(map(int, input().split())))
arr.sort(key=lambda x: x[-1])

cycle_table = [i for i in range(n + 1)]

def union(cycle_table, x, y):
    x = find(x)
    y = find(y)
    if x < y:
        cycle_table[y] = x
    else:
        cycle_table[x] = y

def find(a):
    if cycle_table[a] != a:
        return find(cycle_table[a])
    return cycle_table[a]

result = 0
for x,y,c in arr:
    if find(x) != find(y):
        result += c
        union(cycle_table,x,y)
print(result)