import collections
n,m,v = map(int, input().split())
arr = []
for _ in range(m):
    arr.append(list(map(int, input().split())))
print(sorted(arr, key=lambda x:x[0][0]))
graph = {}
for i in range(len(arr)):
    if arr[i][0] not in graph:
        temp = []
        temp.append(arr[i][1])
        graph[arr[i][0]] = set(temp) 
    else:
        temp.append(arr[i][1])
        del graph[arr[i][0]]
        graph[arr[i][0]] = set(temp)
print(graph)
for i in range(len(arr)):
    if arr[i][1] not in graph:
        temp = []
        temp.append(arr[i][0])
        graph[arr[i][1]] = set(temp) 
    else:
        temp.append(arr[i][0])
        del graph[arr[i][1]]
        graph[arr[i][1]] = set(temp)
print(graph)

def dfs(graph, start):
    visit = list()
    stack = list()

    stack.append(start)

    while stack:
        print(stack)
        node = min(stack)
        stack.remove(node)
        if node not in visit:
            visit.append(node)
            stack = []
            stack.extend(graph[node])
    return visit

def bfs(graph, start):
    visit = list()
    queue = list()

    queue.append(start)

    while queue:
        node = queue.pop(0)
        if node not in visit:
            visit.append(node)
            queue.extend(graph[node])
    return visit

print(dfs(graph, v))
# print(bfs(graph, v))