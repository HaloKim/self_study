# 로또의 최고 순위와 최저 순위.py
def solution(lottos, win_nums):
    ans = [6,6,5,4,3,2,1]
    cnt = 0
    
    for i in win_nums:
        if i in lottos:
            cnt += 1
    
    return [ans[cnt+lottos.count(0)], ans[cnt]]