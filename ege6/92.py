def func(s):
    n = 0
    while s > 0:
        s = s - 5
        n = n + 2
    return n

max = 0

for s in range(1,1000):
    if func(s) == 150:
        max = s

print(max)