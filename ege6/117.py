def func(d):
    n = 20
    s = 40
    while s+n < d:
        s = s -10
        n = n -20
    return n

k = 0

for d in range(1,1000):
    if func(d) > 0:
        k += 1
        print(d)