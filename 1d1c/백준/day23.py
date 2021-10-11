# 1541
n = input()
op = []
for i in n:
    if not i.isdigit():
        op.append(i)
n = n.replace('-', ' ')
n = n.replace('+', ' ')
n = list(map(int, n.split()))
for i in range(len(op)):
    for j in range(i+1,len(op)):
        if op[i] == '-':
            while(op[j] == '+'):
                op[j] = '-'

minimum = n.pop(0)
for i in op:
    a = n.pop(0)
    if i == '-':
        minimum -= a
    if i == '+':
        minimum += a
print(minimum)