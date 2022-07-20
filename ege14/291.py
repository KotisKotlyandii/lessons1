def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]

for x in range(2,10000):
    a = 125 ** 7 - 25 ** 4 + x
    if f(a,5).count(4) == 15 and f(a,5).count(3) == 1 and f(a,5).count(1) == 2:
        print(x)