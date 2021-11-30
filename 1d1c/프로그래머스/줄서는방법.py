def factorial(n):
    v = 1
    for i in range(1, n+1):
        v *= i
    return v

def solution(n, k):
    answer = []
    lst = [x for x in range(1, n+1)]
    
    while lst:
        temp = factorial(n-1)
        q, r = divmod(k, temp)
        q = q-1 if r == 0 else q
        
        answer.append(lst.pop(q))
        
        n -= 1
        k = r
        
    return answer