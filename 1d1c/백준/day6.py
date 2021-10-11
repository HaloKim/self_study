# 2231
'''
n = input()
setup = 0
for i in range(0,1000000):
    if setup != 0:
        break
    total = 0
    for j in list(map(int,str(i))):
        total += j
    if total + i == int(n):
        setup = i
print(setup)
'''

# 1018 어려워서 모르겠다.
'''
n,m = map(int,input().split())
board = []
count = []

for _ in range(n):
    board.append(input())
for i in range(n-7):
    for j in range(m-7):
        w = 0
        b = 0
        for k in range(i, i+8):
            for h in range(j, j+8):
                if (k+h) % 2 == 0:
                    if board[k][h] != 'W':
                        w += 1
                    if board[k][h] != 'B':
                        b += 1
                else :
                    if board[k][h] != 'B':
                        w += 1
                    if board[k][h] != 'W':
                        b += 1
        count.append(min(w,b))
print(min(count))
'''

#1932
n = input()
tri = []
total = 0
arr = []
for _ in range(int(n)):
    tri.append(input().split())
if len(tri) == 1:
    pass
else:
    for i in range(1, len(tri)):
        for j in range(len(tri[i])):
            if j == 0:
                tri[i][j] = int(tri[i][j]) + int(tri[i-1][0])
            elif j == len(tri[i])-1:
                tri[i][j] = int(tri[i][j]) + int(tri[i-1][len(tri[i-1])-1])
            else:
                if int(tri[i-1][j-1]) > int(tri[i-1][j]):
                    tri[i][j] = int(tri[i][j]) + int(tri[i-1][j-1])
                else:
                    tri[i][j] = int(tri[i][j]) + int(tri[i-1][j])
print(max(tri[len(tri)-1]))