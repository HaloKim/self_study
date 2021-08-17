# 12865 어렵다
n, k = map(int,input().split())

arr = [[0,0]]
for _ in range(n):
	arr.append(list(map(int,input().split())))

table = [[0]*(k+1) for i in range(n+1)]
for i in range(1,n+1):
	for j in range(1,k+1):
		w = arr[i][0]
		v = arr[i][1]
		if j < w:
			table[i][j] = table[i-1][j]
		else:
			table[i][j] = max(v + table[i-1][j-w], table[i-1][j])
print(max(table[-1]))