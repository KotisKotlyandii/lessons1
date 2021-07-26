def func(s):
    n = 200
    while s // n >= 2:
        s = s + 5
        n = n + 5
    return s

max = 0

for s in range(100,1000):
    if func(s) > 100:
        max = s

print(max)