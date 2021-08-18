def func(s):
    n = 5
    while s > 5:
        s = s // 2
        n = n+4
    return n

max = 0

for s in range(1,1000):
    if func(s) == 29:
        max = s

print(max)