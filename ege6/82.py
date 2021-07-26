def func(s):
    n = 5
    while s < 110:
        n = n + 1
        s = s + n
    return n

max = 0

for s in range(-1000, 1000):
    if func(s) == 15:
        max = s

print(max)
