V = int(input())
arr = [[] for _ in range(V+1)]
for i in range(V):
    a = list(map(int, input().split()))
    for j in range(1, len(a)-1, 2):
        arr[a[0]].append((a[j],a[j+1]))

def dfs(start, ans):
    for e,w in arr[start]:
        if ans[e] == 0:
            ans[e] = ans[start] + w
            dfs(e,ans)

longest = [0]*(V+1)
dfs(1, longest)
print(longest)
longest[1] = 0
maxi = 0
index = 0
for i, x in enumerate(longest):
    if maxi < x:
        maxi = x
        index = i

ans = [0]*(V+1)
dfs(index, ans)
ans[index] = 0
print(max(ans))