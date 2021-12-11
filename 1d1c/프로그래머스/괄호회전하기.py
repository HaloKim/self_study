from collections import deque
def solution(s):
    ans = 0
    s = deque(s)
    for i in range(len(s)):
        s.rotate(-1)
        if found(s):
            ans += 1
    return ans

def found(s):
    stack = []
    for i in s:
        if i in ('[','(','{'):
            stack.append(i)
        else:
            if not stack:
                return 0
            x = stack.pop()
            if i == ')' and x != '(':
                return 0
            elif i == ']' and x != '[':
                return 0
            elif i == '}' and x != '{':
                return 0
    return len(stack) == 0