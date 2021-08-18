def func(s):
    n = 40
    while s+n < 100:
        s =s+25
        n =n-5
    return s

for s in range(1,1000):
    if func(s) == s:
        print(s)
        break