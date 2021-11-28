def solution(n):
    ans = 0
    temp = []
    while n > 0:
        temp.append(n%3)
        n //= 3
    for i in range(len(temp)-1,-1,-1):
        ans += pow(3, len(temp)-i-1) * temp[i]
    return ans