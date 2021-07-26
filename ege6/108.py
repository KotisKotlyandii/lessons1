def func(s):
    n = 10
    while s > n+20:
        s =s-6
        n =n+11
    return n

for s in range(1,1000):
    if func(s) >= 450:
        print(s)
        break