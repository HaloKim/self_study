people = int(input())
times = []
times = input().split()
for i in range(len(times)):
    times[i] = int(times[i])
change = 0
total = 0
temp = []
for i in range(people):
    total += (min(times))
    temp.append(total)
    times.remove(min(times))
print(sum(temp))
