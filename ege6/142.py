def func(s):
    n = 1
    while s > 200:
        s = s - 15
        n = n + 3
    return n

max = 0

for s in range(1,1000):
    if func(s) == 46:
        max = s

print(max)
