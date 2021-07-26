def func(s):
    n = 100
    while s-n >= 100:
        s =s+20
        n =n+40
    return s

for s in range(0,1000):
    if func(s) == s:
        print(s)
        break
