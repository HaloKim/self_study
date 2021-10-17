# 10974re.py
n = int(input())

seq = []
def dfs():
    if len(seq) == n:
        print(*seq)
        return
    for i in range(1,n+1):
        if i not in seq:
            seq.append(i)
            dfs()
            seq.pop()
dfs()