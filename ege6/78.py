def func(s):
    n = 0
    while s+n <= 300:
        s = s-5
        n = n+25
    return n

max = 0

for s in range(1,1000):
    if func(s) == 250:
        max = s

print(max)