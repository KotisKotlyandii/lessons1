def f(x):
    a,b = 0,1
    while x > 0:
        a += 1
        if x % 12 != 0:
            b *= x % 12
        x //= 12
    return a,b

kol = 0

for x in range(1,100000):
    if f(x) == (2,10):
        kol += 1

print(kol)