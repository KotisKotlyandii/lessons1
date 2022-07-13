def f(n):
    a = -1
    k = 0
    while n > 9 and a != n % 10:
        a = n % 10
        n //= 10
        k += 1
    return k,a

for x in range(1,100000):
    if f(x) == (4,7):
        print(x)
        break