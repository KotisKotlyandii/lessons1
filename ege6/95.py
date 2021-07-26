def func(s):
    n = 1
    while s<208:
        s = s+20
        n = n*2
    return n

max = 0

for s in range(1,1000):
    if func(s) == 256:
        max = s

print(max)
