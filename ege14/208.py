def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]

a = 128 ** 30 + 16 ** 60 - 16
print(f(a,8).count(7))