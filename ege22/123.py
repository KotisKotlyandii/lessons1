def f(n):
    a = -1
    while n > 9 and a != n % 10:
        a = n % 10
        n //= 10
    if a == n % 10:
        return a
    else:
        return n

for x in range(100,1000):
    if f(x) == 5:
        print(x)
