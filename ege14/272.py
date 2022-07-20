def f(c, n):
    s = []
    while c != 0:
        s.append(c % n)
        c //= n
    return s[::-1]

a = 15 + 2 ** 10 + 16
print(hex(a))
print(hex(a).count('f'))