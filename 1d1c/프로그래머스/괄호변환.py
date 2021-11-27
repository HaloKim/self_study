def div(p):
    left = 0
    right = 0
    for i in range(len(p)):
        if p[i] == '(':
            left += 1
        else:
            right += 1
        if left == right:
            return p[:i+1], p[i+1:]
def isRight(p):
    arr = []
    for i in p:
        if i == '(':
            arr.append('(')
        else:
            if not arr:
                return 0
            arr.pop()
    return 1
        
def solution(p):
    if not p:
        return ""
    u, v = div(p)
    if isRight(u):
        return u + solution(v)
    else:
        ans = '('
        ans += solution(v)
        ans += ')'
        for i in u[1:-1]:
            if i =='(':
                ans += ')'
            else:
                ans += '('
        return ans