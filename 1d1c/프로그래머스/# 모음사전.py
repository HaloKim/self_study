# 모음사전.py
def solution(word):
    ans = 0
    dict = {"E": 1, "I": 2, "O": 3, "U": 4}
    for i in range(len(word)):
        if word[i] == 'A':
            ans += 1
        else:
            for j in range(4,i,-1):
                ans += pow(5,j-i) * dict[word[i]]
            ans += dict[word[i]] + 1
    return ans