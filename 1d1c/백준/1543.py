docu = input()
find = input()
l = len(find)
cnt = 0
i = 0
while True:
    if i > len(docu):
        break
    if docu[i:i+l] == find:
        cnt += 1
        i += l
    else:
        i += 1
print(cnt)