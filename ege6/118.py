def func(s):
    n = 2
    while s < 45:
        s = s +3
        n = n * 2
    return n

for s in range(1,1000):
    if func(s) == 128:
        print(s)
        break