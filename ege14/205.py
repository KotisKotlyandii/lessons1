def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]

a = 64 ** 30 + 2 ** 300 - 32
print(f(a,4).count(3))