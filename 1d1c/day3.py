'''
#11720
count = input()
arr = []
num = input()
arr = [int(i) for i in num]
print(sum(arr))
'''
'''
#2675
T = 0
R = 0
S = []
T = int(input())
for i in range(T):
    temp = []
    R,S = input().split()
    new_S = []
    new_S = [tmp for tmp in S]
    for j in range(len(new_S)):
        for k in range(int(R)):
            temp.append(new_S[j])
    print(''.join(temp))
'''

#1157
def find_key(dict, val):
  return next(key for key, value in dict.items() if value == val).upper()
words = input()
temp = [i.lower() for i in words]
dic = {}
for i in temp:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
count = 0
for i in dic.values():
    if i == max(dic.values()):
        count += 1
if count > 1:
    print("?")
else:
    print(find_key(dic, max(dic.values())))


    
