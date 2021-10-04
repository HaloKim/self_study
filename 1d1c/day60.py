# 3190 
n = int(input())
k = int(input())
board = [[0]*n for _ in range(n)]
for i in range(k):
    x,y = map(int,input().split())
    board[x-1][y-1] = 1

l = int(input())
rotate = [list(input().split()) for _ in range(l)]

def right(time,size,x,y,position):
    i = x
    for j in range(y+1,n):
        time += 1
        if [i,j] in position:
            print(time)
            return
        for w in range(size-1,-1,-1):
            if w == 0:
                position[w] = [i, j]
            else:
                position[w] = [position[w-1][0], position[w-1][1]]
        if board[i][j] == 1:
            board[i][j] = 0
            size += 1
            position.append([i,j-1])
        for t,m in rotate:
            if time == int(t) and m == 'D':
                rotate.pop(0)
                down(time, size, i, j, position)
                return
            elif time == int(t) and m == 'L':
                rotate.pop(0)
                up(time, size, i, j, position)
                return
    else:
        print(time+1)
        return

def down(time,size,x,y,position):
    j = y
    for i in range(x+1,n):
        time += 1
        if [i,j] in position:
            print(time)
            return
        for w in range(size-1,-1,-1):
            if w == 0:
                position[w] = [i, j]
            else:
                position[w] = [position[w-1][0], position[w-1][1]]
        if board[i][j] == 1:
            board[i][j] = 0
            size += 1
            position.append([i-1,j])
        for t,m in rotate:
            if time == int(t) and m == 'D':
                rotate.pop(0)
                left(time, size, i, j, position)
                return
            elif time == int(t) and m == 'L':
                rotate.pop(0)
                right(time, size, i, j, position)
                return
    else:
        print(time+1)
        return

def up(time,size,x,y,position):
    j = y
    for i in range(x-1,-1,-1):
        time += 1
        if [i,j] in position:
            print(time)
            return
        for w in range(size-1,-1,-1):
            if w == 0:
                position[w] = [i, j]
            else:
                position[w] = [position[w-1][0], position[w-1][1]]
        if board[i][j] == 1:
            board[i][j] = 0
            size += 1
            position.append([i+1,j])
        for t,m in rotate:
            if time == int(t) and m == 'D':
                rotate.pop(0)
                right(time, size, i, j, position)
                return
            elif time == int(t) and m == 'L':
                rotate.pop(0)
                left(time, size, i, j, position)
                return
    else:
        print(time+1)
        return

def left(time,size,x,y,position):
    i = x
    for j in range(y-1,-1,-1):
        time += 1
        if [i,j] in position:
            print(time)
            return
        for w in range(size-1,-1,-1):
            if w == 0:
                position[w] = [i, j]
            else:
                position[w] = [position[w-1][0], position[w-1][1]]
        if board[i][j] == 1:
            board[i][j] = 0
            size += 1
            position.append([i,j+1])
        for t,m in rotate:
            if time == int(t) and m == 'D':
                rotate.pop(0)
                up(time, size, i, j, position)
                return
            elif time == int(t) and m == 'L':
                rotate.pop(0)
                down(time, size, i, j, position)
                return
    else:
        print(time+1)
        return

position = [[0,0]]
right(0,1,0,0,position)

'''
8
5
6 1
7 3
3 5
5 7
5 6
12
2 D
8 D
10 D
12 D
18 L
20 L
22 L
24 L
25 L
28 L
32 D
33 L
'''