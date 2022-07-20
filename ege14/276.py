def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]

a = 100 ** 2 + 625 ** 25 + 5 ** 100
print(f(a,15).count(12))