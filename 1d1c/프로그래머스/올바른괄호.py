def solution(s):
    stack = []
    for i in s:
        if i == '(':
            stack.append('(')
        else:
            if not stack or stack.pop() == ')':
                return False
    if stack:
        return False
    return True