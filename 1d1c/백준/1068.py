N = int(input())
arr = list(map(int, input().split()))
tree = [[] for _ in range(N)]
sub = int(input())

def dfs(x):
    global ans
    if not tree[x]:
        ans += 1
        return
    for v in tree[x]:
        dfs(v)

for i in range(N):
    if arr[i] == -1:
        root = i
        continue
    if i == sub:
        continue
    tree[arr[i]].append(i)

ans = 0
if root != sub:
    dfs(root)
print(ans)