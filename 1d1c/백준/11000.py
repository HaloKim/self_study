import heapq

n = int(input())
time = []
for i in range(n):
    a,b = map(int,input().split())
    time.append([a,b])
time.sort()
hq = []
heapq.heappush(hq,time[0][1])

for i in range(1,n):
    if hq[0] > time[i][0]:
        heapq.heappush(hq, time[i][1])
    else:
        heapq.heappop(hq)
        heapq.heappush(hq, time[i][1])
print(len(hq))