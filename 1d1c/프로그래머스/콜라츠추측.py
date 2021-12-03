def fun(num,cnt):
    global ans
    if num == 1:
        ans = cnt
        return
    elif cnt > 500:
        ans = -1
        return
    elif num%2 == 0:
        fun(num//2, cnt+1)
    else:
        fun(num*3+1, cnt+1)

def solution(num):
    global ans
    fun(num,0)
    return ans