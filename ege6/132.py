def func(s):
    n = 12
    while s > 0:
        s = s - 10
        n = n + 7
    return n

max = 0

for s in range(1,1000):
    if func(s) == 61:
        max = s

print(max)