def solution(s):
    ans = list(map(int, s.split(' ')))
    ans = str(min(ans)) + ' ' + str(max(ans))
    return ans