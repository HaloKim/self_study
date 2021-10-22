# 조이스틱.py
def solution(name):
    name = list(name)
    cnt = 0
    i = 0
    while True:
        if i != 'A':
            cnt += min(ord(name[i])-ord('A'), ord('Z')-ord(name[i])+1)
        name[i] = 'A'
        if name.count('A') == len(name) : 
            return cnt
        
        left, right = 1, 1
        for j in range(1, len(name)):
            if name[i-j] != 'A':
                break
            left += 1
        for j in range(1, len(name)):
            if name[i+j] != 'A':
                break
            right += 1
        if left < right:
            cnt += left
            i -= left
        else:
            cnt += right
            i += right
    return cnt