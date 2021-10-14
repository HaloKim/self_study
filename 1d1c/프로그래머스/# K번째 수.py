# K번째 수
def solution(array, commands):
    answer = []
    for s,e,f in commands:
        tmp = []
        for i in range(s-1,e):
            tmp.append(array[i])
        tmp.sort()
        for i in tmp:
            f -= 1
            if f == 0:
                answer.append(i)
    return answer