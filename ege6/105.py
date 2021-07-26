def func(s):
    n = 0
    while s+n < 450:
        s =s-5
        n =n+25
    return n

for s in range(1,1000):
    if func(s) <= 50:
        print(s)
        break