def solution(s):
    arr = ['zero','one','two','three','four','five','six','seven','eight','nine']
    ans = ''
    temp = ''
    for i in s:
        if temp in arr:
            ans += str(arr.index(temp))
            temp = ''
        if '0' <= i <= '9':
            ans += str(i)
        else:
            temp += i
    if temp in arr:
            ans += str(arr.index(temp))
    return int(ans)