# 신규아이디추천.py
import re

def solution(new_id):
    ans = ''
    ans = re.sub('[^a-z\d\-\_\.]', '', new_id.lower())
    ans = re.sub('\.\.+', '.', ans)
    ans = re.sub('^\.|\.$', '', ans)
    if ans == '':
        ans = 'a'
    ans = re.sub('\.$', '', ans[0:15])
    while len(ans) < 3:
        ans += ans[-1]
    return ans