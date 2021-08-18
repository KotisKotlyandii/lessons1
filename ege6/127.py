def func(s):
    n = 2
    while s < 64:
        s = s+8
        n = n*2
    return n

max = 0

for s in range(1,1000):
    if func(s) == 256:
        max = s

print(max)