def f(n):
    i = 0
    while n > 0:
        i += n % 8
        n //= 8
    return i%7
kol = 0
for x in range(10,100):
    if f(x) == 0:
        kol += 1

print(kol)