# 1963 매우어려웠다.
n = int(input())

prime = [1]*10001
def isnotprime(data):
    for i in range(1,10001):
        for j in range(2,i):
            if i%j == 0 and i != j:
                prime[i] = 0
                break
isnotprime(prime)

def bfs(a,b):
    queue = []
    queue.append([a,0])
    visit = [0 for _ in range(10000)]
    visit[a] = 1
    while queue:
        v, count = queue.pop(0)
        if v == b:
            return count
        if v < 1000:
                continue
        for i in [1,10,100,1000]:
            tmp = v - v % (i * 10) // i * i
            for j in range(10):
                if visit[tmp] == 0 and prime[tmp] == 1:
                    queue.append([tmp,count+1])
                    visit[tmp] = 1
                tmp += i

for i in range(n):
    a, b = map(int, input().split())
    count = bfs(a,b)
    print(count if count != None else 'Impossible')