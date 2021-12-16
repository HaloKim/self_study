def solution(N, stages):
    total = len(stages)
    fail = 0
    ans = []
    for i in range(1,N+1):
        fail = stages.count(i)
        if fail == 0:
            ans.append([i,0])
        else:
            ans.append([i,fail/total])
        total -= fail
    ans.sort(key = lambda x:x[-1], reverse = True)
    return [i[0] for i in ans]