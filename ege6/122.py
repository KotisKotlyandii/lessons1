def func(s):
    n = 1
    while s < 200:
        s = s + 25
        n = n * 2
    return n

k = 1
min = 0
max = 0

for s in range(1,1000):
    if func(s) == 64:
        if k == 1:
            min = s
            k += 1
            continue
        max = s

print(min+max)
