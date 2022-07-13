def f(n):
    i = 0
    while n > 0:
        i += n % 16
        n //= 16
    return i%15

for x in range(10,100):
    if f(x) == 0:
        print(x)
        break