def solution(s):
    ans = s[2:-2]
    ans = ans.split('},{')
    ans.sort(key = len)
    answer = []
    for i in ans:
        for j in i.split(','):
            j = int(j)
            if j not in answer:
                answer.append(j)
    return answer