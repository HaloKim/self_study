# 6603
def dfs(k,s,i):
    global visit
    if len(q) == 6:
        print(*q)
        return
    for j in range(i,len(s)):
        if visit[s[j]] == 0:
            visit[s[j]] += 1
            q.append(s[j])
            dfs(k,s,j+1)
            q.pop()
            visit[s[j]] = 0
    return

while(True):
    tmp = list(map(int, input().split()))
    k = tmp.pop(0)
    if k == 0:
        break
    s = tmp
    visit = [0]*50
    q = []
    dfs(k,s,0)
    print()