def func(s):
    n = 400
    while s-n > 0:
        s =s-20
        n =n-15
    return s

for s in range(1,1000):
    if func(s) < 0:
        print(s)
        break