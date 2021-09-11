# 9252 어렵다 ..
import sys

n = [0] + list(sys.stdin.readline().strip())
m = [0] + list(sys.stdin.readline().strip())

LCS = [[""]*len(m) for _ in range(len(n))]

for i in range(1, len(n)):
    for j in range(1, len(m)):
        if n[i] == m[j]:
            LCS[i][j] = LCS[i-1][j-1] + n[i]
        else:
            if len(LCS[i-1][j]) > len(LCS[i][j-1]):
                LCS[i][j] = LCS[i-1][j]
            else:
                LCS[i][j] = LCS[i][j-1]
print(len(LCS[-1][-1]))
print(LCS[-1][-1])