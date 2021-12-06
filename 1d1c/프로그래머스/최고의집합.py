def solution(n, s):
    if n <= s:
        p,r = divmod(s,n)
        arr = [p for _ in range(n)]
        for i in range(r):
            arr[i] += 1
        arr.sort()
        return arr
    else:
        return [-1]