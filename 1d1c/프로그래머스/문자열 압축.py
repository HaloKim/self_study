# 문자열 압축.py
def solution(s):
    answer = []
    if len(s)==1: 
        return 1
    for i in range(1, (len(s)//2)+1):
        ans = ''
        cnt = 1
        temp = s[:i]
        for j in range(i,len(s),i):
            if temp == s[j:i+j]:
                cnt += 1
            else:
                if cnt != 1:
                    ans = ans + str(cnt) + temp
                else:
                    ans = ans + temp
                temp = s[j:j+i]
                cnt = 1
        if cnt != 1:
            ans = ans + str(cnt) + temp
        else:
            ans = ans + temp
        answer.append(len(ans))
    return min(answer)