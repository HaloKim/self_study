# 섬연결하기.py
def solution(n, costs):
    ans = 0
    costs.sort(key = lambda x: x[-1])
    find = set([costs[0][0]])
    while len(find) != n:
        for i, v in enumerate(costs):
            if v[0] in find and v[1] in find:
                continue
            if v[0] in find or v[1] in find:
                find.update([v[0], v[1]])
                ans += v[-1]
                costs[i] = [-1,-1,-1]
                break
    return ans