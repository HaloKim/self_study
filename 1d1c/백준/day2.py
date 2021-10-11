'''
#15596
def solve(a):
    ans = sum(a)
    return ans
'''
'''
#4673
arr = [False for i in range(10001)]
num_sum = []
def d(num):
    temp = num
    n_sum = 0
    if num >= 1000:
        n_sum = n_sum + num//1000
        num = num%1000
    if num >= 100:
        n_sum = n_sum + num//100
        num = num%100
    if num >= 10:
        n_sum = n_sum + num//10
        num = num%10
    if num >= 1:
        n_sum = n_sum + num//1
        num = num%1
    return int(n_sum+temp)
for i in range(len(arr)):
    if d(i) < len(arr):
        arr[d(i)] = True
for i in range(len(arr)):
    if arr[i] == False:
        print(i)
'''
