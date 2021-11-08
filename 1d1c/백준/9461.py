t = int(input())
arr = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
for _ in range(t):
    pn = int(input())
    if pn > len(arr):
        while len(arr) != pn:
            arr.append(arr[-1] + arr[len(arr)-5])
        print(arr[-1])
    else:
        print(arr[pn-1])