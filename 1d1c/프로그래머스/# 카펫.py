# 카펫
def solution(brown, yellow):
    answer = []
    for i in range(1,yellow+1):
        temp = yellow//i
        if (i+2) * (temp + 2) == brown + yellow:
            if i+2 >= temp + 2:
                answer = [i+2, temp + 2]
                break
    return answer