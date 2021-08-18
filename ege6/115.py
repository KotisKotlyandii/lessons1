def func(S):
    S = S // 8
    N = 2
    while S <= 102:
        S = S + 4
        N = N * 2 - 1
    return N

max = 0

for S in range(1,1000):
    if func(S) == 257:
        max = S

print(max)