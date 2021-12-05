def solution(absolutes, signs):
    ans = []
    for i in range(len(absolutes)):
        if signs[i]:
            ans.append(absolutes[i])
        else:
            ans.append(-absolutes[i])
    return sum(ans)