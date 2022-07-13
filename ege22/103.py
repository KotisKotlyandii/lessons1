def f(x):
    a,b = 0,1
    while x > 0:
        a += 1
        b *= x % 10
        x //= 10
    return a,b
kol = 0
for x in range(1,10000):
    if f(x) == (2,0):
        kol += 1

print(kol)