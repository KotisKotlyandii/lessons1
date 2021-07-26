def func(n):
    s = 350
    while 2*s+n < 1100:
        s = s - 5
        n = n + 15
    return s

max = 0

for n in range(1,1000):
    if func(n) == 45:
        max = n

print(max)