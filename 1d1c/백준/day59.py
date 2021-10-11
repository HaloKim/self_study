# 12100 매우어렵다..
import copy

n = int(input())
init_board = [list(map(int, input().split())) for _ in range(n)]

def up(board):
    for i in range(n):
        p = 0
        before = 0
        for j in range(n):
            if board[j][i] == 0:
                continue
            if before == 0:
                before = board[j][i]
            else:
                if before == board[j][i]:
                    board[p][i] = before*2
                    p += 1
                    before = 0
                else:
                    board[p][i] = before
                    p += 1
                    before = board[j][i]
            board[j][i] = 0
        if before != 0: 
            board[p][i] = before
    return board

def down(board):
    for i in range(n):
        p = n-1
        before = 0
        for j in range(n-1,-1,-1):
            if board[j][i] == 0:
                continue
            if before == 0:
                before = board[j][i]
            else:
                if before == board[j][i]:
                    board[p][i] = before*2
                    p -= 1
                    before = 0
                else:
                    board[p][i] = before
                    p -= 1
                    before = board[j][i]
            board[j][i] = 0
        if before != 0: 
            board[p][i] = before
    return board

def left(board):
    for i in range(n):
        p = 0
        before = 0
        for j in range(n):
            if board[i][j] == 0:
                continue
            if before == 0:
                before = board[i][j]
            else:
                if before == board[i][j]:
                    board[i][p] = before*2
                    p += 1
                    before = 0
                else:
                    board[i][p] = before
                    p += 1
                    before = board[i][j]
            board[i][j] = 0
        if before != 0: 
            board[i][p] = before
    return board

def right(board):
    for i in range(n):
        p = n-1
        before = 0
        for j in range(n-1,-1,-1):
            if board[i][j] == 0:
                continue
            if before == 0:
                before = board[i][j]
            else:
                if before == board[i][j]:
                    board[i][p] = before*2
                    p -= 1
                    before = 0
                else:
                    board[i][p] = before
                    p -= 1
                    before = board[i][j]
            board[i][j] = 0
        if before != 0: 
            board[i][p] = before
    return board
            
maxi = 0
def dfs(board, cnt):
    global maxi
    if cnt == 5:
        for i in range(n):
            for j in range(n):
                maxi = max(board[i][j], maxi)
        return

    dfs(up(copy.deepcopy(board)), cnt+1)
    dfs(down(copy.deepcopy(board)), cnt+1)
    dfs(left(copy.deepcopy(board)), cnt+1)
    dfs(right(copy.deepcopy(board)), cnt+1)

dfs(init_board, 0)
print(maxi)