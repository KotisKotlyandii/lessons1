def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]

a = 32 ** 30 + 8 ** 60 - 32
print(f(a,4).count(3))