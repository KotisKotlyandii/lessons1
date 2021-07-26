def func(s):
    n = 1
    while s < 185:
        s = s + 30
        n = n * 3
    return n

k = 1
min = 0
max = 0

for s in range(1,2000):
    if func(s) == 729:
        if k == 1:
            min = s
            k += 1
            continue
        max = s

print(str(max)+str(min))