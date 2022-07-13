def f(n):
    a = - 1
    while n > 9 and a != n % 10:
        a = n % 10
        n //= 10
    return n % 10

for x in range(1000, 10000):
    if f(x) == 4:
        print(x)
        break