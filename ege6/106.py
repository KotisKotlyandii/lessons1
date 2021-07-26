def func(s):
    n = 80
    while s+n < 160:
        s = s+15
        n = n-10
    return s

max = 0

for s in range(-100,10000):
    if func(s) <= 100:
        max = s

print(max)