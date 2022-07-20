def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]

a = 16 ** 20 + 2 ** 30 - 32
print(f(a,4).count(3))