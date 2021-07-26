def func(s):
    n = 1
    while s < 28:
        s = s+5
        n = n*3
    return n

for s in range(1,1000):
    if func(s) == 81:
        print(s)
        break