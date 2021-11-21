R,C = map(int, input().split())
start = [-1,0]
if R == 1:
    print(1)
elif R == 2:
    print(min(4, (C+1)//2))
elif C <= 6:
    print(min(4, C))
else:
    print(C-2)