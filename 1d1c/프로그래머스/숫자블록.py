import math
def solution(begin, end):
    ans = []
    for i in range(begin,end+1):
        if i == 1:
            ans.append(0)
            continue
        else:
            for j in range(2, int(math.sqrt(end))+1):
                if i//j > int(1e7):
                    continue
                if i%j == 0:
                    ans.append(i//j)
                    break
            else:
                ans.append(1)
    return ans