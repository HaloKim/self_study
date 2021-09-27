# 14888
n = int(input())

num = list(map(int, input().split()))
a,b,c,d = map(int, input().split()) # + - * /

maxi = -1000000000
mini = 1000000000
def dfs(number,idx,add,sub,multi,division):
    global maxi, mini
    if idx == n:
        maxi = max(number,maxi)
        mini = min(number,mini)
        return
    else:
        if add:
            dfs(number + num[idx], idx+1, add-1,sub,multi,division)
        if sub:
            dfs(number - num[idx], idx+1, add,sub-1,multi,division)
        if multi:
            dfs(number * num[idx], idx+1, add,sub,multi-1,division)
        if division:
            dfs(int(number / num[idx]), idx+1, add,sub,multi,division-1)
dfs(num[0],1,a,b,c,d)
print(maxi,mini, sep='\n')