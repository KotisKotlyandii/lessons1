def func(s):
    n = 1
    while s < 28:
        s = s + 5
        n = n * 3
    return n

max = 0

for s in range(-100,1000):
    if func(s) == 81:
        max = s

print(max)
