def func(s):
    n = -5
    while s > 10:
        s = s - 8
        n = n + 3
    return n

k = 1
min = 0
max = 0

for s in range(1,1000):
    if func(s) == 67:
        if k == 1:
            min = s
            k += 1
        max = s

print(str(max)+str(min))