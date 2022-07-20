def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]

a = 64 ** 30 + 2 ** 300 - 4
print(f(a,8).count(7))