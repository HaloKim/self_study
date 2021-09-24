# 4796
import sys

tmp = []
while True:
    l,p,v = map(int, sys.stdin.readline().strip().split())
    if v == 0:
        break
    if v%p <= l:
        sum = (v//p)*l + (v%p)
    elif v%p > l:
        sum =(v//p)*l + l
    tmp.append(sum)

for i in range(len(tmp)):
    print("Case %d:" %(i+1), tmp[i])