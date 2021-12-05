def solution(numbers):
    ans = []
    for i in range(1,10):
        if i not in numbers:
            ans.append(i)
    return sum(ans)