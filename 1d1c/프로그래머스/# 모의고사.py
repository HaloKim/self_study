# 모의고사
def solution(answers):
    ans = []
    man1 = [1,2,3,4,5]
    man2 = [2,1,2,3,2,4,2,5]
    man3 = [3,3,1,1,2,2,4,4,5,5]
    a1,a2,a3 = 0,0,0
    for i in range(len(answers)):
        index = answers[i]
        if index == man1[i%5]:
            a1 += 1
        if index == man2[i%8]:
            a2 += 1
        if index == man3[i%10]:
            a3 += 1
    m = max(a1,a2,a3)
    if m == a1:
        ans.append(1)
    if m == a2:
        ans.append(2)
    if m == a3:
        ans.append(3)
    return ans