def solution(s):
    stack = []
    for i in s:
        if stack and stack[-1] == i:
            stack.pop()
            continue
        stack.append(i)
    if not stack:
        return 1
    return 0