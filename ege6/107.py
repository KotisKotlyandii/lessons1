def func(s):
    n = 80
    while s+n < 160:
        s =s+15
        n =n-10
    return s

for s in range(-10000,1000):
    if func(s) <= 100:
        print(s)
        break