# 13458
n = int(input()) # 시험장수
A = list(map(int, input().split())) # 각 시험장 응시자수
B,C = map(int,input().split()) # 감독 부감독

cnt = n
for i in A:
    i -= B
    if i > 0:
        if i % C:
            cnt += (i//C) + 1
        else:
            cnt += (i//C)
print(cnt)