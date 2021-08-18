def func(s):
    n = 121
    while s < 124:
        s = s +10
        n = n +17
    return n

max = 0

for s in range(1,1000):
    if func(s) == 291:
        max = s

print(max)