def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]

a = 125 + 25**3 + 5 ** 9
print(f(a,5).count(0))