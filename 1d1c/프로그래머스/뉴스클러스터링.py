def solution(str1, str2):
    str1 = find_set(str1)
    str2 = find_set(str2)
    inter = set(str1) & set(str2)
    union = set(str1) | set(str2)
    if len(union) == 0:
        return 65536
    interlen = sum([min(str1.count(i), str2.count(i)) for i in inter])
    unionlen = sum([max(str1.count(i), str2.count(i)) for i in union])
    return int((interlen / unionlen) * 65536)

def find_set(strs):
    arr = []
    for i in range(len(strs)-1):
        if strs[i].isalpha() and strs[i+1].isalpha():
            arr.append(strs[i:i+2].upper())
    return arr