def f(x):
    a,b = 0,1
    while x > 0:
        a += 1
        if x % 8 != 1:
            b *= x % 8
        x //= 8
    return a,b

kol = 0

for x in range(1,100000):
    if f(x) == (3,24):
        kol += 1

print(kol)