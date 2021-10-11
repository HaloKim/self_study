from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    ans = 0
    q = deque()
    q.append((begin,0))
    while q:
        print(q)
        v,index = q.popleft()
        for w in words:
            compare = 0
            for j in range(len(w)):
                if v[j] != w[j]:
                    compare += 1
            if compare == 1 and w == target:
                index += 1
                return index
            elif compare == 1:
                q.append((w,index+1))
    return ans