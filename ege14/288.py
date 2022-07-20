def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]

for x in range(2,10000):
    a = 36 ** 17 - 6 ** x + 71
    if sum(f(a,6)) == 61:
        print(x)