def f(x):
    a,b = 0,1
    while x > 0:
        a += 1
        if x % 14 != 0:
            b *= x % 14
        x //= 14
    return a,b

kol = 0

for x in range(1,100000):
    if f(x) == (2,12):
        kol += 1

print(kol)