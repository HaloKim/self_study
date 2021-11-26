def solution(gems):
    check = len(set(gems))
    gemdict = {}
    start = 0
    end = 0
    maxi = len(gems) + 1
    ans = []
    while end < len(gems):
        if gems[end] not in gemdict:
            gemdict[gems[end]] = 1
        else:
            gemdict[gems[end]] += 1
        end += 1
        if len(gemdict) == check:
            while start < end:
                if gemdict[gems[start]] > 1:
                    gemdict[gems[start]] -= 1
                    start += 1
                elif end-start < maxi:
                    maxi = end-start
                    ans = [start+1, end]
                    break
                else:
                    break
    return ans