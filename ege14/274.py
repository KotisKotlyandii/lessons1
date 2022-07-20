def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]

a = 26 ** 2 + 169 - 11
print(f(a,13).count(12) + f(a,13).count(2))