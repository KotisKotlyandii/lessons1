def func(d):
    n = 1
    while d//n > 0:
        d = d - 2
        n = n + 3
    return n

k = 1
min = 0
max = 0

for s in range(1,1000):
    if func(s) == 46:
        if k == 1:
            min = s
            k += 1
            continue
        max = s

print(min+max)

