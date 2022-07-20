def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]

a = 32 ** 60 + 4 ** 180 - 128
print(f(a,8).count(7))