#9934
k = int(input())
room = []
room = input().split()
tree = [[] for _ in range(k)]

def maketree(arr, x):
    mid = (len(arr)//2)
    tree[x].append(arr[mid])
    if len(arr) == 1:
        return
    maketree(arr[:mid], x+1)
    maketree(arr[mid+1:], x+1)
maketree(room, 0)

for i in range(len(tree)):
    print(*tree[i])
