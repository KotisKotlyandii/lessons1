def f(x):
    a, b = 0, 0
    while x > 0:
        a += 1
        b = x % 9
        x //= 9
    return a, b


kol = 0

for x in range(1, 100000):
    if f(x) == (5, 7):
        kol += 1

print(kol)