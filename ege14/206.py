def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]

a = 64 ** 150 + 4 ** 300 - 32
print(f(a,8).count(7))