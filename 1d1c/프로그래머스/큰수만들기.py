# 큰수만들기.py
def solution(number, k):
    ans = [number[0]]
    for i in number[1:]:
        if k > 0:
            while ans[-1] < i:
                ans.pop()
                k -= 1
                if not ans or k == 0:
                    break
        ans.append(i)
    if k != 0:
        ans = ans[:-k]
    return ''.join(ans)