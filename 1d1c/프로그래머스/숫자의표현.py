def solution(n):
    ans = 0
    for i in range(n,0,-1):
        temp = 0
        for j in range(i,0,-1):
            temp += j
            if temp > n:
                break
            if temp == n:
                ans += 1
                break
    return ans