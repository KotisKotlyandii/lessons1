def f(n):
    i = 0
    while n > 0:
        i += n % 9
        n //= 9
    return i%8
kol = 0
for x in range(10,100):
    if f(x) != 0:
        print(x)
        break