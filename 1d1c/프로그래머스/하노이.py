def solution(n):
    ans = []
    hanoi(n,1,3,2,ans)
    return ans

def hanoi(n,n1,n3,n2,ans):
    if n == 1:
        return ans.append([n1,n3])
    else:
        hanoi(n-1,n1,n2,n3,ans)
        ans.append([n1,n3])
        hanoi(n-1,n2,n3,n1,ans)