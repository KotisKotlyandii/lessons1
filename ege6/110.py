def func(s):
    n = 127
    while s-n > 0:
        s =s+15
        n =n+20
    return s

for s in range(1,1000):
    if func(s) >= 1000:
        print(s)
        break