def f(n):
    i = 0
    while n > 0:
        i += n % 20
        n //= 20
    return i%19

for x in range(100,1000):
    if f(x) == 0:
        print(x)
        break