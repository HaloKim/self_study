def solution(nums):
    how = len(nums)//2
    ans = list(set(nums))
    return len(ans[:how])